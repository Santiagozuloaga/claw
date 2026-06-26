import sys, os, tempfile
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import pytest

def test_generate_unified_diff():
    import importlib; _mod = importlib.import_module('2024-06-19_CLAW_TOOLS_V01'); globals().update({k: getattr(_mod, k) for k in ['generate_unified_diff']})
    old = "line1\nline2\nline3\n"
    new = "line1\nline2_modified\nline3\n"
    diff = generate_unified_diff(old, new, "test.py")
    assert "--- a/test.py" in diff
    assert "+++ b/test.py" in diff
    assert "-line2" in diff
    assert "+line2_modified" in diff

def test_generate_unified_diff_empty_old():
    import importlib; _mod = importlib.import_module('2024-06-19_CLAW_TOOLS_V01'); globals().update({k: getattr(_mod, k) for k in ['generate_unified_diff']})
    diff = generate_unified_diff("", "new content\n", "test.py")
    assert "+new content" in diff

def test_edit_returns_diff(tmp_path):
    import importlib; _mod = importlib.import_module('2024-06-19_CLAW_TOOLS_V01'); globals().update({k: getattr(_mod, k) for k in ['_edit']})
    f = tmp_path / "test.txt"
    f.write_text("hello world\n")
    result = _edit(str(f), "hello", "goodbye")
    assert "-hello world" in result
    assert "+goodbye world" in result

def test_write_existing_returns_diff(tmp_path):
    import importlib; _mod = importlib.import_module('2024-06-19_CLAW_TOOLS_V01'); globals().update({k: getattr(_mod, k) for k in ['_write']})
    f = tmp_path / "test.txt"
    f.write_text("old content\n")
    result = _write(str(f), "new content\n")
    assert "-old content" in result
    assert "+new content" in result

def test_write_new_file_no_diff(tmp_path):
    import importlib; _mod = importlib.import_module('2024-06-19_CLAW_TOOLS_V01'); globals().update({k: getattr(_mod, k) for k in ['_write']})
    f = tmp_path / "new.txt"
    result = _write(str(f), "content\n")
    assert "Created" in result
    assert "---" not in result

def test_diff_truncation():
    import importlib; _mod = importlib.import_module('2024-06-19_CLAW_TOOLS_V01'); globals().update({k: getattr(_mod, k) for k in ['generate_unified_diff', 'maybe_truncate_diff']})
    old = "\n".join(f"line{i}" for i in range(200))
    new = "\n".join(f"CHANGED{i}" for i in range(200))
    diff = generate_unified_diff(old, new, "big.py")
    truncated = maybe_truncate_diff(diff, max_lines=50)
    assert "more lines" in truncated
    assert truncated.count("\n") < 60
