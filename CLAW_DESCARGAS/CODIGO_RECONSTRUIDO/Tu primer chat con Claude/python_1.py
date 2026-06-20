if sys.platform == "win32":
    os.system("")  # Enable ANSI escape codes on Windows CMD
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    ...