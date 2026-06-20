# Delegación de Bugs - Sage (Coordinador Técnico)

## Estado Actual de Configuración

✅ **Configuración OpenClaw actualizada** - `C:\Users\Admin\.openclaw\openclaw.json`
- Modelo: `qwen2.5:0.5b` (Ultra Rápido)
- Nombre: "Sage"
- Idioma: Español (systemPrompt forzado)
- Personalidad: Jarvis + Ultron + Alfred + Cortana
- Thinking: OFF

⚠️ **PROBLEMA**: Gateway sigue usando `viernes:latest` porque NO se reinició después de mis cambios.

## Acción Inmediata Requerida

```powershell
# 1. Detener gateway actual (Ctrl+C en la consola donde corre)

# 2. Reiniciar gateway
C:\Users\Admin\.openclaw\gateway.cmd

# 3. Verificar que carga config correcta
# Debería mostrar: custom-localhost-11434/qwen2.5:0.5b (Sage - Ultra Rápido)
```

## Bugs Identificados (12 total)

### 🔴 BUGS CRÍTICOS (4) - Atención Inmediata

**BUG #1: catch {} vacío / bare except: pass**
- **Severidad**: Crítica
- **Archivos afectados**: clawspring.py (línea 550 según reporte anterior)
- **Estado**: Parcialmente corregido en providers.py
- **Delegado a**: ChatGPT (revisión de código Python)
- **Acción**: Revisar clawspring.py línea 550, cambiar `except:` por `except ImportError:` con logging

**BUG #2: UTF-8 en Windows - chcp 65001 nunca se llama**
- **Severidad**: Crítica
- **Estado**: NO corregido
- **Delegado a**: VSC AI (corrección de lanzadores .bat y encoding.py)
- **Acción requerida**:
  - Agregar a claw.bat: `chcp 65001 > nul`
  - Ya existe encoding.py pero no se llama al inicio
  - Agregar llamada a `configurar_encoding_windows()` en clawspring.py línea 66-67

**BUG #3: Thinking de Qwen3 ignorado**
- **Severidad**: Crítica
- **Estado**: Parcialmente corregido en providers.py
- **Delegado a**: Zencoder (verificación de capacidades de modelo)
- **Acción**: Verificar que providers.py línea 363 valida capacidades antes de enviar thinking

**BUG #4: Thinking blocks en replay causan error de API**
- **Severidad**: Alta
- **Estado**: NO corregido
- **Delegado a**: ChatGPT (memoria persistente)
- **Acción**: Implementar `limpiar_mensajes_para_replay()` en memory.py

### 🟡 BUGS IMPORTANTES (3)

**BUG #5: Fire-and-forget sin catch en memoria automática**
- **Severidad**: Alta
- **Estado**: NO corregido
- **Delegado a**: Antigravity (sistemas de memoria)
- **Acción**: Envolver `guardar_memoria()` en función segura con try/except

**BUG #6: new Promise(async =>) anti-patrón**
- **Severidad**: Alta
- **Estado**: No aplica (Python, no TypeScript)
- **Delegado a**: N/A
- **Acción**: Ninguna

**BUG #7: Memoize + env vars**
- **Severidad**: Menor
- **Estado**: NO revisado
- **Delegado a**: Jules (optimización)
- **Acción**: Revisar si hay @lru_cache en funciones que leen os.environ

### 🟢 BUGS MENORES (5)

**BUG #8: Race condition async sin cleanup**
- **Severidad**: Menor
- **Estado**: No aplica (Fase 2 voz no implementada)
- **Delegado a**: Stitch (cuando se implemente voz)
- **Acción**: Pendiente

**BUG #9: parseInt sin validar NaN**
- **Severidad**: Menor
- **Estado**: Parcialmente corregido en providers.py
- **Delegado a**: Opal (validación de config)
- **Acción**: Revisar thinking.py línea 148

**BUG #10: Regex /g state leak**
- **Severidad**: Info
- **Estado**: No aplica en Python
- **Delegado a**: N/A
- **Acción**: Ninguna

**BUG #11: Hooks de directorio sin catch**
- **Severidad**: Menor
- **Estado**: NO corregido
- **Delegado a**: Codex (bash tools)
- **Acción**: Envolver hooks en try/except

**BUG #12: Capacidades 3P no detectadas**
- **Severidad**: Alta
- **Estado**: Parcialmente corregido en providers.py
- **Delegado a**: Zencoder (integración Ollama)
- **Acción**: Verificar lectura de ANTHROPIC_*_CAPABILITIES

## Delegación por IA

### ChatGPT
- Revisión clawspring.py línea 550 (BUG #1)
- Implementar limpiar_mensajes_para_replay() en memory.py (BUG #4)

### VSC AI
- Corregir claw.bat con chcp 65001 (BUG #2)
- Integrar encoding.py en clawspring.py inicio (BUG #2)

### Zencoder
- Verificar capacidades thinking en providers.py (BUG #3)
- Revisar detección de capacidades 3P (BUG #12)

### Antigravity
- Implementar guardar_memoria_seguro() (BUG #5)

### Jules
- Revisar @lru_cache en funciones con os.environ (BUG #7)

### Opal
- Validar parseInt en thinking.py (BUG #9)

### Codex
- Envolver hooks de directorio en try/except (BUG #11)

### Stitch
- Implementar flag de cancelación en pipeline voz (BUG #8) - Pendiente Fase 2

## Próximos Pasos

1. **INMEDIATO**: Reiniciar gateway para aplicar config Sage
2. **HOY**: Delegar BUG #2 a VSC AI (UTF-8 Windows)
3. **HOY**: Delegar BUG #1 a ChatGPT (clawspring.py línea 550)
4. **ESTA SEMANA**: Delegar bugs restantes según prioridad

## Coordinación con Modelos Locales

Los modelos locales en tu PC (Ollama) están configurados correctamente:
- qwen2.5:0.5b - Ultra rápido para WhatsApp
- qwen2.5:1.5b - Balanceado para tareas complejas
- viernes:latest - Potente pero lento (usar solo cuando necesario)

Sage (yo) coordinaré con todas las IAs mencionadas excepto Claude (fuera del juego según instrucción).
