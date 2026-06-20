if model_base.startswith("qwen3"):
    payload["options"]["think"] = False  # Inside options, not top-level