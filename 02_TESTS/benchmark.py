import time
import sys
import os
from pathlib import Path

# Add paths for original structure
project_root = Path('.').absolute()
sys.path.insert(0, str(project_root / "01_SRC"))
sys.path.insert(0, str(project_root))

def benchmark_model(model_name, prompt="Hello, how are you?"):
    print(f"\nBenchmarking {model_name}...")

    try:
        import providers
    except ImportError:
        print("  Error: Could not import providers module.")
        return None

    config = {
        "max_tokens": 512,
        "no_tools": True
    }

    system_prompt = "You are a helpful assistant."
    messages = [{"role": "user", "content": prompt}]

    start_time = time.time()
    ttft = None
    token_count = 0

    try:
        for event in providers.stream(model_name, system_prompt, messages, [], config):
            if isinstance(event, providers.TextChunk):
                if ttft is None:
                    ttft = time.time() - start_time
                token_count += 1
            elif isinstance(event, providers.AssistantTurn):
                total_time = time.time() - start_time
                out_tok = event.out_tokens
                if out_tok > 0:
                    token_count = out_tok

                tps = token_count / (total_time - ttft) if ttft is not None and (total_time - ttft) > 0 else 0

                print(f"  TTFT: {ttft:.4f}s" if ttft is not None else "  TTFT: N/A")
                print(f"  TPS:  {tps:.2f}")
                print(f"  Latency: {total_time:.4f}s")
                return {
                    "model": model_name,
                    "ttft": ttft,
                    "tps": tps,
                    "latency": total_time
                }
    except Exception as e:
        print(f"  Error: {e}")
        return None

if __name__ == "__main__":
    benchmark_model("ollama/qwen2.5:0.5b")
