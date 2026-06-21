# CLAW - ClawSpring v3.05.5 (P.A.R.A. + ISO-SAGE)

**Versión**: 3.05.5  
**Fecha**: 2024-06-20  
**Estándar**: P.A.R.A. + ISO-SAGE  
**Tests**: 239 passed

## 📁 Estructura del Proyecto (P.A.R.A.)

```
CLAW_FINAL/
├── 00_SOPORTE/              # Configuraciones, requisitos, entorno y logs
│   ├── CLAW_2024_06_19_CONFIG_V01.py
│   ├── CLAW_2024_06_19_GITIGNORE_V01
│   ├── CLAW_2024_06_19_PYPROJECT_V01.toml
│   └── CLAW_2024_06_19_REQUIREMENTS_V01.txt
├── 01_SRC/                  # Lógica principal del asistente (ClawSpring v3.05.5)
│   ├── CLAW_2024_06_19_CORE_V01.py
│   ├── CLAW_2024_06_19_AGENT_V01.py
│   ├── CLAW_2024_06_19_PROVIDERS_V01.py
│   ├── CLAW_2024_06_19_TOOLS_V01.py
│   ├── CLAW_2024_06_19_CONTEXT_V01.py
│   ├── mcp/, memory/, multi_agent/, plugin/, skill/, task/, voice/
├── 02_TESTS/                # Pruebas unitarias y de integración
│   ├── test_compaction.py
│   ├── test_memory.py
│   └── ... (239 tests passed)
├── 03_DOCS/                 # Documentación, manuales y archivos históricos
│   ├── README_CLAWSPRING.md
│   ├── CLAW_ARCHIVE_DOCS/
│   └── README-CN.md
├── 04_ASSETS/               # Recursos estáticos, imágenes y demos
│   ├── demos/
│   ├── logo-2.png
│   └── screenshot.png
├── run_claw.py              # Lanzador en la raíz
├── .clinerules              # Reglas de programación E-SYSTEM
└── README.md                # Este archivo
```

## 🚀 Ejecución

### Requisitos
- Python 3.12+
- Ollama (para modelos locales)
- OpenClaw Gateway (para WhatsApp)

### Instalación

```powershell
# Instalar dependencias
pip install -r 00_SOPORTE/CLAW_2024_06_19_REQUIREMENTS_V01.txt

# Configurar Ollama
ollama pull qwen2.5:3b
```

### Ejecución

```powershell
# Ejecutar con lanzador raíz
python run_claw.py

# O ejecutar directamente
python 01_SRC/CLAW_2024_06_19_CORE_V01.py
```

### Configuración OpenClaw

El archivo de configuración está en:
```
C:\Users\Admin\.openclaw\openclaw.json
```

**Configuración actual (Sage)**:
- Modelo: `viernes:latest` (Potente)
- Nombre: "Sage"
- Idioma: Español
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
- **Antigravity**: Sistemas memoria (hasta 25/6)
- **Jules**: Optimización, performance
- **Opal**: Validación configuración
- **Codex**: Bash tools, hooks (hasta julio)
- **Stitch**: Pipeline voz (Fase 2)
- **Devin**: Disponible para colaborar
- **Aider**: Disponible

Claude está excluido del juego.

## 🔧 Seguridad Física

Si el script supera los 50 minutos de ejecución, añade un log de 'alerta de enfriamiento'.

## 📚 Documentación

- `03_DOCS/README_CLAWSPRING.md` - Documentación completa de ClawSpring v3.05.5
- `.clinerules` - Reglas de programación E-SYSTEM

## 🎯 Fases del Proyecto

- **Fase 1**: Python ClawSpring v3.05.5 - ✅ COMPLETADA
- **Fase 2**: Voz (Whisper) - ⏳ Pendiente
- **Fase 3**: Telegram - ⏳ Pendiente
- **Fase 4**: Multi-sesión - ⏳ Pendiente

---
*Merge de trabajo Jules + Sage - 2024-06-20*
