# Cortana- Asistente Personal IA

**Versión**: 3.05.5  
**Fecha**: 2024-06-19  
**Estándar**: P.A.R.A. + ISO-SAGE

## 📁 Estructura del Proyecto (P.A.R.A.)

```
CLAW_FINAL/
├── 00_SOPORTE/              # Logs, configuraciones, .env
│   ├── config.py
│   ├── claw.bat
│   ├── .gitignore
│   └── LICENSE
├── 01_SRC/                  # Código lógico (separado por módulos)
│   ├── 2024-06-19_CLAW_CLAWSPRING_CORE_V01.py
│   ├── 2024-06-19_CLAW_AGENT_CORE_V01.py
│   ├── 2024-06-19_CLAW_PROVIDERS_V01.py
│   ├── 2024-06-19_CLAW_TOOLS_V01.py
│   ├── 2024-06-19_CLAW_MEMORY_V01.py
│   ├── 2024-06-19_CLAW_THINKING_V01.py
│   ├── 2024-06-19_CLAW_ENCODING_V01.py
│   ├── 2024-06-19_CLAW_ERROR_UTILS_V01.py
│   ├── 2024-06-19_CLAW_MAIN_V01.py
│   ├── 2024-06-19_CLAW_PERSONALIDAD_V01.py
│   ├── 2024-06-19_CLAW_MEMORY_PACKAGE_V01/
│   ├── 2024-06-19_CLAW_MULTI_AGENT_V01/
│   ├── 2024-06-19_CLAW_SKILL_V01/
│   ├── 2024-06-19_CLAW_MCP_V01/
│   ├── 2024-06-19_CLAW_PLUGIN_V01/
│   ├── 2024-06-19_CLAW_TASK_V01/
│   └── 2024-06-19_CLAW_VOICE_V01/
├── 02_TESTS/                # Pruebas automatizadas
│   └── 2024-06-19_CLAW_TESTS_V01/
├── 03_DOCS/                 # Documentación técnica
│   ├── 2024-06-19_CLAW_DOCS_V01/
│   ├── 2024-06-19_CLAW_DEMOS_V01/
│   ├── README.md
│   ├── README_JULES.md
│   ├── SAGE_DELEGACION_BUGS.md
│   ├── INSTRUCCIONES_SAGE.md
│   └── claw_historial.html
├── 04_ASSETS/               # Recursos estáticos
│   ├── 2024-06-19_CLAW_TEMP_UPLOAD_V01/
│   └── 2024-06-19_CLAW_PYCACHE_V01/
├── .clinerules              # Reglas de programación E-SYSTEM
└── README.md                # Este archivo
```

## 🚀 Ejecución según P.A.R.A.

### Requisitos
- Python 3.12+
- Ollama (para modelos locales)
- OpenClaw Gateway (para WhatsApp)

### Instalación

```powershell
# Instalar dependencias
cd 01_SRC
pip install -r ../00_SOPORTE/requirements.txt

# Configurar Ollama
ollama pull qwen2.5:0.5b
```

### Ejecución

```powershell
# Ejecutar Claw principal
cd 01_SRC
python 2024-06-19_CLAW_MAIN_V01.py

# O usar el lanzador
cd 00_SOPORTE
claw.bat
```

### Configuración OpenClaw

El archivo de configuración está en:
```
C:\Users\Admin\.openclaw\openclaw.json
```

**Configuración actual (Sage)**:
- Modelo: `qwen2.5:0.5b` (Ultra Rápido)
- Nombre: "Sage"
- Idioma: Español (forzado)
- Personalidad: Jarvis + Ultron + Alfred + Cortana
- Thinking: OFF

## 📋 Nomenclatura ISO-SAGE

Todo archivo nuevo debe seguir:
`[AAAA-MM-DD]_[PROYECTO]_[DESCRIPCIÓN]_V[XX].[ext]`

Ejemplos:
- `2024-06-19_CLAW_CLAWSPRING_CORE_V01.py`
- `2024-06-19_CLAW_MEMORY_V01.py`

## 🤖 Coordinación con IAs

Sage coordina con:
- **ChatGPT**: Revisión código, bugs críticos
- **VSC AI**: Corrección lanzadores, encoding
- **Zencoder**: Integración Ollama, capacidades
- **Antigravity**: Sistemas memoria
- **Jules**: Optimización, performance
- **Opal**: Validación configuración
- **Codex**: Bash tools, hooks
- **Stitch**: Pipeline voz (Fase 2)

Claude está excluido del juego.

## 🐛 Bugs Delegados

**🔴 Críticos**:
- BUG #1 (catch {} vacío) → ChatGPT
- BUG #2 (UTF-8 Windows) → VSC AI
- BUG #3 (Thinking Qwen3) → Parcialmente corregido
- BUG #4 (Thinking blocks replay) → ChatGPT

**🟡 Importantes**:
- BUG #5 (Fire-and-forget memoria) → Antigravity
- BUG #7 (Memoize + env vars) → Jules
- BUG #12 (Capacidades 3P) → Parcialmente corregido

Ver `03_DOCS/SAGE_DELEGACION_BUGS.md` para detalles completos.

## 🔧 Seguridad Física

Si el script supera los 50 minutos de ejecución, añade un log de 'alerta de enfriamiento'.

## 📚 Documentación

- `03_DOCS/README.md` - Documentación original
- `03_DOCS/README_JULES.md` - Guía para Jules
- `03_DOCS/SAGE_DELEGACION_BUGS.md` - Delegación de bugs
- `03_DOCS/INSTRUCCIONES_SAGE.md` - Instrucciones de activación
- `03_DOCS/claw_historial.html` - Visualizador de historial

## 🎯 Fases del Proyecto

- **Fase 1**: Python ClawSpring - ✅ COMPLETADA
- **Fase 2**: Voz (Whisper) - ⏳ Pendiente
- **Fase 3**: Telegram - ⏳ Pendiente
- **Fase 4**: Multi-sesión - ⏳ Pendiente

## 📞 Soporte

Sage (Coordinador Técnico) - Asistente personal IA con personalidad combinada de Jarvis, Ultron, Alfred y Cortana.
