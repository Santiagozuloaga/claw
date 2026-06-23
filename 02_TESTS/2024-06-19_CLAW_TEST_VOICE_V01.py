"""Tests for the voice/ package (no hardware required).

All tests run without a microphone or STT library installed.
They cover the pure-Python helpers: WAV wrapping, keyterm extraction,
availability checks, and the REPL integration sentinel.
"""
from __future__ import annotations

import struct
import sys
from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest

# ── Helpers ───────────────────────────────────────────────────────────────

def _make_pcm(n_samples: int = 1600) -> bytes:
    """Return silent int16 PCM (all zeros)."""
    return b"\x00\x00" * n_samples


# ── voice.keyterms ────────────────────────────────────────────────────────

class TestSplitIdentifier:
    def test_camel_case(self):
        import importlib
        m_2024_06_19_CLAW_VOICE_V01_2024_06_19_CLAW_KEYTERMS_V01 = importlib.import_module("2024-06-19_CLAW_VOICE_V01.2024-06-19_CLAW_KEYTERMS_V01")
        globals().update({'split_identifier': getattr(m_2024_06_19_CLAW_VOICE_V01_2024_06_19_CLAW_KEYTERMS_V01, 'split_identifier')})
        assert split_identifier("nanoClaudeCode") == ["nano", "Claude", "Code"]

    def test_kebab_case(self):
        import importlib
        m_2024_06_19_CLAW_VOICE_V01_2024_06_19_CLAW_KEYTERMS_V01 = importlib.import_module("2024-06-19_CLAW_VOICE_V01.2024-06-19_CLAW_KEYTERMS_V01")
        globals().update({'split_identifier': getattr(m_2024_06_19_CLAW_VOICE_V01_2024_06_19_CLAW_KEYTERMS_V01, 'split_identifier')})
        result = split_identifier("my-webhook-handler")
        assert "webhook" in result
        assert "handler" in result

    def test_snake_case(self):
        import importlib
        m_2024_06_19_CLAW_VOICE_V01_2024_06_19_CLAW_KEYTERMS_V01 = importlib.import_module("2024-06-19_CLAW_VOICE_V01.2024-06-19_CLAW_KEYTERMS_V01")
        globals().update({'split_identifier': getattr(m_2024_06_19_CLAW_VOICE_V01_2024_06_19_CLAW_KEYTERMS_V01, 'split_identifier')})
        result = split_identifier("my_project_root")
        assert "project" in result
        assert "root" in result

    def test_short_fragments_dropped(self):
        import importlib
        m_2024_06_19_CLAW_VOICE_V01_2024_06_19_CLAW_KEYTERMS_V01 = importlib.import_module("2024-06-19_CLAW_VOICE_V01.2024-06-19_CLAW_KEYTERMS_V01")
        globals().update({'split_identifier': getattr(m_2024_06_19_CLAW_VOICE_V01_2024_06_19_CLAW_KEYTERMS_V01, 'split_identifier')})
        result = split_identifier("a-bb-ccc")
        # "a" and "bb" are ≤2 chars and should be dropped
        assert "a" not in result
        assert "bb" not in result
        assert "ccc" in result

    def test_path_like(self):
        import importlib
        m_2024_06_19_CLAW_VOICE_V01_2024_06_19_CLAW_KEYTERMS_V01 = importlib.import_module("2024-06-19_CLAW_VOICE_V01.2024-06-19_CLAW_KEYTERMS_V01")
        globals().update({'split_identifier': getattr(m_2024_06_19_CLAW_VOICE_V01_2024_06_19_CLAW_KEYTERMS_V01, 'split_identifier')})
        result = split_identifier("src/services/voice.ts")
        assert "services" in result
        assert "voice" in result


class TestGetVoiceKeyterms:
    def test_returns_list(self):
        import importlib
        m_2024_06_19_CLAW_VOICE_V01_2024_06_19_CLAW_KEYTERMS_V01 = importlib.import_module("2024-06-19_CLAW_VOICE_V01.2024-06-19_CLAW_KEYTERMS_V01")
        globals().update({'get_voice_keyterms': getattr(m_2024_06_19_CLAW_VOICE_V01_2024_06_19_CLAW_KEYTERMS_V01, 'get_voice_keyterms')})
        terms = get_voice_keyterms()
        assert isinstance(terms, list)

    def test_global_terms_present(self):
        import importlib
        m_2024_06_19_CLAW_VOICE_V01_2024_06_19_CLAW_KEYTERMS_V01 = importlib.import_module("2024-06-19_CLAW_VOICE_V01.2024-06-19_CLAW_KEYTERMS_V01")
        globals().update({'get_voice_keyterms': getattr(m_2024_06_19_CLAW_VOICE_V01_2024_06_19_CLAW_KEYTERMS_V01, 'get_voice_keyterms'), 'GLOBAL_KEYTERMS': getattr(m_2024_06_19_CLAW_VOICE_V01_2024_06_19_CLAW_KEYTERMS_V01, 'GLOBAL_KEYTERMS')})
        terms = get_voice_keyterms()
        # At least half of global terms should appear
        overlap = sum(1 for t in GLOBAL_KEYTERMS if t in terms)
        assert overlap >= len(GLOBAL_KEYTERMS) // 2

    def test_max_length(self):
        import importlib
        m_2024_06_19_CLAW_VOICE_V01_2024_06_19_CLAW_KEYTERMS_V01 = importlib.import_module("2024-06-19_CLAW_VOICE_V01.2024-06-19_CLAW_KEYTERMS_V01")
        globals().update({'get_voice_keyterms': getattr(m_2024_06_19_CLAW_VOICE_V01_2024_06_19_CLAW_KEYTERMS_V01, 'get_voice_keyterms'), 'MAX_KEYTERMS': getattr(m_2024_06_19_CLAW_VOICE_V01_2024_06_19_CLAW_KEYTERMS_V01, 'MAX_KEYTERMS')})
        terms = get_voice_keyterms()
        assert len(terms) <= MAX_KEYTERMS

    def test_deduplication(self):
        import importlib
        m_2024_06_19_CLAW_VOICE_V01_2024_06_19_CLAW_KEYTERMS_V01 = importlib.import_module("2024-06-19_CLAW_VOICE_V01.2024-06-19_CLAW_KEYTERMS_V01")
        globals().update({'get_voice_keyterms': getattr(m_2024_06_19_CLAW_VOICE_V01_2024_06_19_CLAW_KEYTERMS_V01, 'get_voice_keyterms')})
        terms = get_voice_keyterms()
        assert len(terms) == len(set(terms)), "Duplicate keyterms found"

    def test_recent_files_passed(self):
        import importlib
        m_2024_06_19_CLAW_VOICE_V01_2024_06_19_CLAW_KEYTERMS_V01 = importlib.import_module("2024-06-19_CLAW_VOICE_V01.2024-06-19_CLAW_KEYTERMS_V01")
        globals().update({'get_voice_keyterms': getattr(m_2024_06_19_CLAW_VOICE_V01_2024_06_19_CLAW_KEYTERMS_V01, 'get_voice_keyterms')})
        terms = get_voice_keyterms(recent_files=["src/authentication_handler.py"])
        assert "authentication" in terms or "handler" in terms


# ── voice.stt ─────────────────────────────────────────────────────────────

class TestPcmToWav:
    def test_riff_header(self):
        import importlib
        m_2024_06_19_CLAW_VOICE_V01_2024_06_19_CLAW_STT_V01 = importlib.import_module("2024-06-19_CLAW_VOICE_V01.2024-06-19_CLAW_STT_V01")
        globals().update({'_pcm_to_wav': getattr(m_2024_06_19_CLAW_VOICE_V01_2024_06_19_CLAW_STT_V01, '_pcm_to_wav')})
        wav = _pcm_to_wav(_make_pcm(1600))
        assert wav[:4] == b"RIFF"
        assert wav[8:12] == b"WAVE"
        assert wav[12:16] == b"fmt "

    def test_data_chunk(self):
        import importlib
        m_2024_06_19_CLAW_VOICE_V01_2024_06_19_CLAW_STT_V01 = importlib.import_module("2024-06-19_CLAW_VOICE_V01.2024-06-19_CLAW_STT_V01")
        globals().update({'_pcm_to_wav': getattr(m_2024_06_19_CLAW_VOICE_V01_2024_06_19_CLAW_STT_V01, '_pcm_to_wav')})
        pcm = _make_pcm(1600)
        wav = _pcm_to_wav(pcm)
        # data chunk starts at byte 36
        assert wav[36:40] == b"data"
        data_size = struct.unpack_from("<I", wav, 40)[0]
        assert data_size == len(pcm)

    def test_roundtrip_length(self):
        import importlib
        m_2024_06_19_CLAW_VOICE_V01_2024_06_19_CLAW_STT_V01 = importlib.import_module("2024-06-19_CLAW_VOICE_V01.2024-06-19_CLAW_STT_V01")
        globals().update({'_pcm_to_wav': getattr(m_2024_06_19_CLAW_VOICE_V01_2024_06_19_CLAW_STT_V01, '_pcm_to_wav')})
        pcm = _make_pcm(800)
        wav = _pcm_to_wav(pcm)
        # WAV = 44-byte header + pcm data
        assert len(wav) == 44 + len(pcm)


class TestKeytermsToPrompt:
    def test_empty(self):
        import importlib
        m_2024_06_19_CLAW_VOICE_V01_2024_06_19_CLAW_STT_V01 = importlib.import_module("2024-06-19_CLAW_VOICE_V01.2024-06-19_CLAW_STT_V01")
        globals().update({'_keyterms_to_prompt': getattr(m_2024_06_19_CLAW_VOICE_V01_2024_06_19_CLAW_STT_V01, '_keyterms_to_prompt')})
        assert _keyterms_to_prompt([]) == ""

    def test_contains_terms(self):
        import importlib
        m_2024_06_19_CLAW_VOICE_V01_2024_06_19_CLAW_STT_V01 = importlib.import_module("2024-06-19_CLAW_VOICE_V01.2024-06-19_CLAW_STT_V01")
        globals().update({'_keyterms_to_prompt': getattr(m_2024_06_19_CLAW_VOICE_V01_2024_06_19_CLAW_STT_V01, '_keyterms_to_prompt')})
        p = _keyterms_to_prompt(["grep", "TypeScript", "MCP"])
        assert "grep" in p
        assert "TypeScript" in p
        assert "MCP" in p

    def test_truncates_at_40(self):
        import importlib
        m_2024_06_19_CLAW_VOICE_V01_2024_06_19_CLAW_STT_V01 = importlib.import_module("2024-06-19_CLAW_VOICE_V01.2024-06-19_CLAW_STT_V01")
        globals().update({'_keyterms_to_prompt': getattr(m_2024_06_19_CLAW_VOICE_V01_2024_06_19_CLAW_STT_V01, '_keyterms_to_prompt')})
        terms = [f"term{i}" for i in range(100)]
        prompt = _keyterms_to_prompt(terms)
        # should not contain term40 or beyond
        assert "term40" not in prompt
        assert "term39" in prompt


class TestSttAvailability:
    def test_returns_tuple(self):
        import importlib
        m_2024_06_19_CLAW_VOICE_V01_2024_06_19_CLAW_STT_V01 = importlib.import_module("2024-06-19_CLAW_VOICE_V01.2024-06-19_CLAW_STT_V01")
        globals().update({'check_stt_availability': getattr(m_2024_06_19_CLAW_VOICE_V01_2024_06_19_CLAW_STT_V01, 'check_stt_availability')})
        result = check_stt_availability()
        assert isinstance(result, tuple)
        assert len(result) == 2

    def test_backend_name_string(self):
        import importlib
        m_2024_06_19_CLAW_VOICE_V01_2024_06_19_CLAW_STT_V01 = importlib.import_module("2024-06-19_CLAW_VOICE_V01.2024-06-19_CLAW_STT_V01")
        globals().update({'get_stt_backend_name': getattr(m_2024_06_19_CLAW_VOICE_V01_2024_06_19_CLAW_STT_V01, 'get_stt_backend_name')})
        name = get_stt_backend_name()
        assert isinstance(name, str)

    @patch.dict("os.environ", {"OPENAI_API_KEY": "sk-test"})
    def test_openai_api_available_when_key_set(self):
        # With faster-whisper/openai-whisper absent but key present → available
        with patch.dict(sys.modules, {"faster_whisper": None, "whisper": None}):
            import importlib
            m_2024_06_19_CLAW_VOICE_V01_2024_06_19_CLAW_STT_V01 = importlib.import_module("2024-06-19_CLAW_VOICE_V01.2024-06-19_CLAW_STT_V01")
            globals().update({'check_stt_availability': getattr(m_2024_06_19_CLAW_VOICE_V01_2024_06_19_CLAW_STT_V01, 'check_stt_availability')})
            ok, _ = check_stt_availability()
            assert ok is True

    @patch.dict("os.environ", {}, clear=True)
    def test_unavailable_without_backends(self):
        with patch.dict(sys.modules, {"faster_whisper": None, "whisper": None}):
            import importlib
            m_2024_06_19_CLAW_VOICE_V01_2024_06_19_CLAW_STT_V01 = importlib.import_module("2024-06-19_CLAW_VOICE_V01.2024-06-19_CLAW_STT_V01")
            globals().update({'check_stt_availability': getattr(m_2024_06_19_CLAW_VOICE_V01_2024_06_19_CLAW_STT_V01, 'check_stt_availability')})
            # If no key either
            import os
            os.environ.pop("OPENAI_API_KEY", None)
            ok, reason = check_stt_availability()
            if not ok:
                assert reason is not None


# ── voice.recorder ────────────────────────────────────────────────────────

class TestRecorderAvailability:
    def test_returns_tuple(self):
        import importlib
        m_2024_06_19_CLAW_VOICE_V01_2024_06_19_CLAW_RECORDER_V01 = importlib.import_module("2024-06-19_CLAW_VOICE_V01.2024-06-19_CLAW_RECORDER_V01")
        globals().update({'check_recording_availability': getattr(m_2024_06_19_CLAW_VOICE_V01_2024_06_19_CLAW_RECORDER_V01, 'check_recording_availability')})
        result = check_recording_availability()
        assert isinstance(result, tuple)
        assert len(result) == 2

    def test_sounddevice_makes_available(self):
        sd_mock = MagicMock()
        with patch.dict(sys.modules, {"sounddevice": sd_mock}):
            import importlib
            m_2024_06_19_CLAW_VOICE_V01_2024_06_19_CLAW_RECORDER_V01 = importlib.import_module("2024-06-19_CLAW_VOICE_V01.2024-06-19_CLAW_RECORDER_V01")
            globals().update({'check_recording_availability': getattr(m_2024_06_19_CLAW_VOICE_V01_2024_06_19_CLAW_RECORDER_V01, 'check_recording_availability')})
            ok, reason = check_recording_availability()
            assert ok is True
            assert reason is None


# ── voice.__init__ ────────────────────────────────────────────────────────

class TestVoiceInit:
    def test_check_voice_deps_returns_tuple(self):
        import importlib
        m_2024_06_19_CLAW_VOICE_V01 = importlib.import_module("2024-06-19_CLAW_VOICE_V01")
        globals().update({'check_voice_deps': getattr(m_2024_06_19_CLAW_VOICE_V01, 'check_voice_deps')})
        result = check_voice_deps()
        assert isinstance(result, tuple)
        assert len(result) == 2

    def test_exports(self):
        import importlib; m_2024_06_19_CLAW_VOICE_V01 = importlib.import_module("2024-06-19_CLAW_VOICE_V01")
        assert hasattr(voice, "check_voice_deps")
        assert hasattr(voice, "voice_input")
        assert hasattr(voice, "transcribe")
        assert hasattr(voice, "get_voice_keyterms")


# ── REPL integration ──────────────────────────────────────────────────────

class TestReplVoiceIntegration:
    def test_voice_in_commands(self):
        import importlib; clawspring = importlib.import_module("2024-06-19_CLAW_CORE_V01")
        assert "voice" in clawspring.COMMANDS

    def test_voice_command_callable(self):
        import importlib; clawspring = importlib.import_module("2024-06-19_CLAW_CORE_V01")
        assert callable(clawspring.COMMANDS["voice"])

    def test_handle_slash_voice_sentinel(self):
        """handle_slash('/voice ...') propagates __voice__ sentinel from cmd_voice."""
        import importlib; clawspring = importlib.import_module("2024-06-19_CLAW_CORE_V01")

        # Patch cmd_voice to return a sentinel directly
        sentinel = ("__voice__", "hello world")
        with patch.object(clawspring, "cmd_voice", return_value=sentinel):
            # Re-bind in COMMANDS so the patch is seen
            clawspring.COMMANDS["voice"] = clawspring.cmd_voice
            result = clawspring.handle_slash("/voice", object(), {})
            assert result == sentinel

    def test_voice_status_no_crash(self, capsys):
        """'/voice status' should not raise even without audio hardware."""
        import importlib; clawspring = importlib.import_module("2024-06-19_CLAW_CORE_V01")
        # Should not raise
        try:
            clawspring.cmd_voice("status", object(), {})
        except SystemExit:
            pass
        # Output captured — just ensure no uncaught exception

    def test_voice_lang_set(self, capsys):
        import importlib; clawspring = importlib.import_module("2024-06-19_CLAW_CORE_V01")
        clawspring.cmd_voice("lang zh", object(), {})
        assert clawspring._voice_language == "zh"
        # Reset
        clawspring.cmd_voice("lang auto", object(), {})
        assert clawspring._voice_language == "auto"
