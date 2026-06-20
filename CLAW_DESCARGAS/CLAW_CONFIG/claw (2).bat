@echo off
chcp 65001 > nul 2>&1
set PYTHONIOENCODING=utf-8
set ANTHROPIC_API_KEY=ollama
title Claw - Asistente IA

REM Liberar RAM antes de arrancar
taskkill /F /IM chrome.exe > nul 2>&1
taskkill /F /IM RobloxPlayerBeta.exe > nul 2>&1
taskkill /F /IM Notion.exe > nul 2>&1
ollama stop qwen3.5:latest > nul 2>&1
ollama stop gemma:latest > nul 2>&1

REM Verificar Ollama activo
curl -s http://localhost:11434/api/tags > nul 2>&1
if errorlevel 1 (
    echo Iniciando Ollama...
    start /B ollama serve
    timeout /t 3 > nul
)

REM Directorio del script
cd /d "%~dp0"

REM Lanzar ClawSpring con modelo viernes
"C:\Users\Admin\AppData\Local\Python\bin\python.exe" clawspring.py --model ollama/viernes:latest %*

if errorlevel 1 (
    echo.
    echo Claw termino con error.
    pause
)
