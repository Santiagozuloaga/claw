def _anthropic_model_supports_thinking(model: str) -> bool:
    """Only send thinking params to Claude models that actually support it."""
    m = model.lower()
    supported = {"claude-opus-4", "claude-sonnet-4", "claude-3-7-sonnet", "claude-3-5-sonnet"}
    return any(s in m for s in supported)