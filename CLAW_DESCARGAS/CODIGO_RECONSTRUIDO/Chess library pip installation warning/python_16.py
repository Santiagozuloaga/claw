# ❌ Antes: Catch genérico
except Exception as e:
    logging.warning(f"Error: {e}")

# ✅ Después: Específico
except (IOError, OSError):
    pass