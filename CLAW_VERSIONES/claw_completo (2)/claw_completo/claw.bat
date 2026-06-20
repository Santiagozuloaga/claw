@echo off
chcp 65001 > nul 2>&1
set PYTHONIOENCODING=utf-8
title Claw - Asistente IA
cd /d "C:\Users\Admin\Downloads\claw_completo"
set ANTHROPIC_API_KEY=ollama
taskkill /F /IM chrome.exe > nul 2>&1
echo Iniciando Claw...
python clawspring.py --model ollama/qwen3.5:latest
if errorlevel 1 pause
