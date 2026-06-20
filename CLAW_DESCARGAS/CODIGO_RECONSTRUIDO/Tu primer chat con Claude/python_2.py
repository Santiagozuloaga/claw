# Before (Bug #3):
if config.get("thinking"):
    kwargs["thinking"] = {
        "type": "enabled",
        "budget_tokens": config.get("thinking_budget", 10000),
    }

# After (safe):
if config.get("thinking") and _anthropic_model_supports_thinking(model):
    budget = config.get("thinking_budget", 10000)
    try:
        budget = int(budget)
        if budget <= 0:
            budget = 10000
    except (ValueError, TypeError):
        budget = 10000
    kwargs["thinking"] = {
        "type": "enabled", 
        "budget_tokens": min(budget, 100000),
    }