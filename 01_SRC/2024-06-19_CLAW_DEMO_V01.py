#!/usr/bin/env python3
"""
Demo script for clawspring.
Requires ANTHROPIC_API_KEY environment variable.

Run:
  ANTHROPIC_API_KEY=sk-... python demo.py
"""
import os
import sys

# Add parent path for imports
sys.path.insert(0, os.path.dirname(__file__))

import importlib

m_2024_06_19_CLAW_CONFIG_V01 = importlib.import_module("2024-06-19_CLAW_CONFIG_V01")

globals().update({'load_config': getattr(m_2024_06_19_CLAW_CONFIG_V01, 'load_config')})
import importlib
m_2024_06_19_CLAW_CONTEXT_V01 = importlib.import_module("2024-06-19_CLAW_CONTEXT_V01")
globals().update({'build_system_prompt': getattr(m_2024_06_19_CLAW_CONTEXT_V01, 'build_system_prompt')})
import importlib
m_2024_06_19_CLAW_AGENT_V01 = importlib.import_module("2024-06-19_CLAW_AGENT_V01")
globals().update({'AgentState': getattr(m_2024_06_19_CLAW_AGENT_V01, 'AgentState'), 'run': getattr(m_2024_06_19_CLAW_AGENT_V01, 'run'), 'TextChunk': getattr(m_2024_06_19_CLAW_AGENT_V01, 'TextChunk'), 'ThinkingChunk': getattr(m_2024_06_19_CLAW_AGENT_V01, 'ThinkingChunk'), 'ToolStart': getattr(m_2024_06_19_CLAW_AGENT_V01, 'ToolStart'), 'ToolEnd': getattr(m_2024_06_19_CLAW_AGENT_V01, 'ToolEnd'), 'TurnDone': getattr(m_2024_06_19_CLAW_AGENT_V01, 'TurnDone'), 'PermissionRequest': getattr(m_2024_06_19_CLAW_AGENT_V01, 'PermissionRequest')})

def demo():
    config = load_config()
    if not config["api_key"]:
        print("Error: Set ANTHROPIC_API_KEY environment variable")
        sys.exit(1)

    config["permission_mode"] = "accept-all"  # Demo: auto-approve everything
    config["verbose"] = True
    state = AgentState()
    system_prompt = build_system_prompt()

    print("=" * 60)
    print("DEMO 1: Simple question (no tools)")
    print("=" * 60)
    _run_demo(state, config, system_prompt,
              "What is the time complexity of quicksort? Answer in 2 sentences.")

    print("\n" + "=" * 60)
    print("DEMO 2: File system exploration (uses Glob + Read tools)")
    print("=" * 60)
    state2 = AgentState()
    _run_demo(state2, config, system_prompt,
              "List all Python files in the current directory and show me the first 5 lines of clawspring.py")

    print("\n" + "=" * 60)
    print("DEMO 3: Code writing (uses Write + Bash tools)")
    print("=" * 60)
    state3 = AgentState()
    _run_demo(state3, config, system_prompt,
              "Write a Python function to fibonacci(n) in /tmp/fib.py, then run it to test fib(10)")

    print("\n" + "=" * 60)
    print("DEMO 4: Multi-turn conversation")
    print("=" * 60)
    state4 = AgentState()
    _run_demo(state4, config, system_prompt,
              "What are the tools available to you?")
    _run_demo(state4, config, system_prompt,
              "Which of those tools would you use to find all TODO comments in a codebase?")

    print("\n" + "=" * 60)
    print("DEMO 5: Web search")
    print("=" * 60)
    state5 = AgentState()
    _run_demo(state5, config, system_prompt,
              "Search the web for 'Python 3.13 new features' and give me a brief summary")


def _run_demo(state: AgentState, config: dict, system_prompt: str, prompt: str):
    print(f"\n[USER]: {prompt}\n")
    print("[CLAUDE]: ", end="", flush=True)

    for event in run(prompt, state, config, system_prompt):
        if isinstance(event, TextChunk):
            print(event.text, end="", flush=True)
        elif isinstance(event, ThinkingChunk):
            if config.get("verbose"):
                print(f"\033[2m[thinking: {event.text[:100]}]\033[0m", end="", flush=True)
        elif isinstance(event, ToolStart):
            print(f"\n\033[36m  ⚙ {event.name}({list(event.inputs.values())[0] if event.inputs else ''})\033[0m", flush=True)
        elif isinstance(event, PermissionRequest):
            event.granted = True  # Auto-approve in demo
        elif isinstance(event, ToolEnd):
            result_preview = event.result[:100].replace('\n', '↵')
            print(f"\033[32m  ✓ → {result_preview}\033[0m", flush=True)
        elif isinstance(event, TurnDone):
            print(f"\n\033[2m  [+{event.input_tokens} in / +{event.output_tokens} out]\033[0m", flush=True)

    print()


if __name__ == "__main__":
    demo()
