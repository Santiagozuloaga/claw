payload = {
    "model": model,
    "messages": oai_messages,
    "stream": True,
    "options": {
        "num_ctx": context_limit
    }
}
# ...
if model_base.startswith("qwen3"):
    payload["think"] = False