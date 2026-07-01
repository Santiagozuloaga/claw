import time
import json
import os
import sys
import argparse
from pathlib import Path

# Add 01_SRC to path
project_root = Path(__file__).parent.parent.absolute()
sys.path.insert(0, str(project_root / "01_SRC"))

from providers import stream, TextChunk, AssistantTurn, list_ollama_models

def benchmark_model(model_name, prompt, iterations=3):
    print(f"\nBenchmarking model: {model_name}")
    results = []

    config = {
        "model": f"ollama/{model_name}",
        "max_tokens": 1024,
        "rich_live": False,
        "verbose": False
    }

    system_prompt = "You are a helpful assistant. Be concise."
    messages = [{"role": "user", "content": prompt}]

    for i in range(iterations):
        print(f"  Iteration {i+1}/{iterations}...", end="", flush=True)
        start_time = time.time()
        first_token_time = None
        total_tokens = 0
        full_text = ""

        try:
            for event in stream(config["model"], system_prompt, messages, [], config):
                if isinstance(event, TextChunk):
                    if first_token_time is None:
                        first_token_time = time.time()
                    full_text += event.text
                    # Rough token estimation: 4 chars = 1 token
                elif isinstance(event, AssistantTurn):
                    # Some providers might return actual token counts
                    pass

            end_time = time.time()
            total_duration = end_time - start_time

            # Estimate tokens if not provided
            total_tokens = len(full_text) / 4

            if first_token_time:
                ttft = first_token_time - start_time
                tps = total_tokens / (end_time - first_token_time) if (end_time - first_token_time) > 0 else 0
            else:
                ttft = total_duration
                tps = total_tokens / total_duration if total_duration > 0 else 0

            results.append({
                "iteration": i + 1,
                "total_duration": total_duration,
                "ttft": ttft,
                "tps": tps,
                "tokens": total_tokens,
                "response_length": len(full_text)
            })
            print(f" Done. TPS: {tps:.2f}, TTFT: {ttft:.2f}s")

        except Exception as e:
            print(f" Failed: {e}")

    if not results:
        return None

    avg_ttft = sum(r["ttft"] for r in results) / len(results)
    avg_tps = sum(r["tps"] for r in results) / len(results)

    return {
        "model": model_name,
        "avg_ttft": avg_ttft,
        "avg_tps": avg_tps,
        "iterations": results
    }

def main():
    parser = argparse.ArgumentParser(description="Ollama Performance Benchmark")
    parser.add_argument("--models", help="Comma-separated list of models to benchmark")
    parser.add_argument("--prompt", default="Write a short story about a cat in 100 words.", help="Prompt to use")
    parser.add_argument("--iter", type=int, default=3, help="Number of iterations")
    parser.add_argument("--output", help="Output JSON file")

    args = parser.parse_args()

    ollama_base_url = "http://localhost:11434"
    available_models = list_ollama_models(ollama_base_url)

    if not available_models:
        print("Error: No Ollama models found. Is Ollama running?")
        sys.exit(1)

    target_models = []
    if args.models:
        target_models = [m.strip() for m in args.models.split(",")]
    else:
        target_models = available_models

    print(f"Starting benchmarks for models: {', '.join(target_models)}")

    all_results = []
    for model in target_models:
        if model not in available_models:
            print(f"Skipping {model}: not found in Ollama.")
            continue

        res = benchmark_model(model, args.prompt, args.iter)
        if res:
            all_results.append(res)

    summary = {
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
        "prompt": args.prompt,
        "results": all_results
    }

    if args.output:
        with open(args.output, "w") as f:
            json.dump(summary, f, indent=2)
        print(f"\nResults saved to {args.output}")
    else:
        # Default output following ISO-SAGE
        out_path = project_root / "03_DOCS" / f"{time.strftime('%Y-%m-%d')}_CLAW_OLLAMA_BENCHMARKS_V01.json"
        with open(out_path, "w") as f:
            json.dump(summary, f, indent=2)
        print(f"\nResults saved to {out_path}")

if __name__ == "__main__":
    main()
