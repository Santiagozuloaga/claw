# REPORTE DE BUGS — Código Fuente Claude Code
## Análisis para el proyecto "Claw" (versión Python)

---

## Resumen ejecutivo

Se analizaron **~200 archivos TypeScript** del repositorio filtrado de Anthropic. Se encontraron **12 categorías de bugs** documentados, organizados por prioridad para la implementación en Python de Claw.

---

## 🔴 BUGS CRÍTICOS (afectan directamente a Claw)

---

### BUG #1 — `catch {}` vacío (errores silenciados completamente)

**Archivos afectados:**
- `src/components/FullscreenLayout.tsx:485` — `catch {}` en `openPath()`: si falla al abrir un archivo, el error desaparece sin rastro
- `src/components/permissions/hooks.ts:180` — `catch {}` en parseo de comandos: errores de parseo silenciados
- `src/server/directConnectManager.ts:72` — `catch {}` en limpieza de sesión
- `src/skills/bundled/claudeApi.ts:35` — `catch {}` sin ningún log

**Equivalente Python que HAY QUE EVITAR en Claw:**
```python
# MAL - equivalente al bug original
try:
    abrir_ruta(url)
except:
    pass   # <- Bug: error silenciado

# BIEN - lo que debe hacer Claw
try:
    abrir_ruta(url)
except Exception as e:
    logger.warning(f"No se pudo abrir ruta: {e}")
```

---

### BUG #2 — `bare except: pass` (el que ya estaban corrigiendo)

Este es el mismo patrón del Bug #1 pero en Python nativo. El código original en TypeScript usa `catch {}` sin body, que en Python se convierte en `except: pass` o `except Exception: pass` sin logging.

**Regla para Claw:** Todo `except` debe loggear al menos una línea a nivel `WARNING` o superior. Nunca silenciar sin registro.

---

### BUG #3 — Thinking de Qwen3 / `think: false` ignorado a veces

**Archivo:** `src/utils/thinking.ts` + `src/services/api/claude.ts:1597-1624`

**El bug:** `shouldEnableThinkingByDefault()` devuelve `true` para proveedores `firstParty` y `foundry`. Para modelos de terceros como Qwen3, el código necesita que la variable de entorno `ANTHROPIC_DEFAULT_*_MODEL_SUPPORTED_CAPABILITIES` esté configurada para saber si el modelo soporta thinking. Si no está configurada, `get3PModelCapabilityOverride()` devuelve `undefined` y el sistema intenta enviar thinking al modelo de todas formas.

**El código problemático en TS:**
```typescript
// claude.ts:1597
if (
  thinkingConfig.type !== 'disabled' &&  // Solo omite si explícitamente disabled
  // ... más checks ...
) {
  // Envía thinking aunque el modelo no lo soporte
}
```

**Corrección para Claw en Python:**
```python
def construir_params_thinking(modelo: str, thinking_config: dict) -> dict:
    """
    Retorna parámetros de thinking seguros para el modelo dado.
    """
    if thinking_config.get("type") == "disabled":
        return {}
    
    # Para modelos de terceros (Qwen, etc.), verificar capacidad explícitamente
    if es_modelo_tercero(modelo):
        capacidades = obtener_capacidades_modelo(modelo)
        if "thinking" not in capacidades and "adaptive_thinking" not in capacidades:
            # El modelo no soporta thinking - NO enviarlo
            return {}
    
    if thinking_config.get("type") == "adaptive":
        return {"type": "adaptive"}
    elif thinking_config.get("type") == "enabled":
        budget = thinking_config.get("budgetTokens", 8000)
        return {"type": "enabled", "budget_tokens": budget}
    
    return {}
```

---

### BUG #4 — UTF-8 en Windows: `chcp 65001` nunca se llama

**Archivo:** `src/utils/Shell.ts`

**El bug:** El código usa `encoding: 'utf8'` para leer archivos, pero **nunca ejecuta `chcp 65001`** antes de iniciar. En Windows, `cmd.exe` por defecto usa CP1252 (Europa Occidental) o CP850 (DOS Latin). Esto causa que caracteres especiales (ñ, á, é, ü, etc.) se rompan.

**Corrección para Claw en Python (CRÍTICO para Windows):**
```python
import sys
import os

def configurar_encoding_windows():
    """Debe llamarse al inicio de Claw en Windows."""
    if sys.platform == "win32":
        # Método 1: Reconfigure I/O streams
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
        sys.stderr.reconfigure(encoding='utf-8', errors='replace')
        sys.stdin.reconfigure(encoding='utf-8', errors='replace')
        
        # Método 2: Variable de entorno para subprocesos
        os.environ['PYTHONIOENCODING'] = 'utf-8'
        
        # Método 3: Ejecutar chcp 65001 para la consola
        os.system('chcp 65001 > nul 2>&1')

# Llamar ANTES de cualquier print() o input()
configurar_encoding_windows()
```

**Para el lanzador `.bat` (Fase 1):**
```batch
@echo off
chcp 65001 > nul
python claw.py %*
```

---

## 🟡 BUGS IMPORTANTES (afectan estabilidad)

---

### BUG #5 — `new Promise<void>(async resolve =>)` anti-patrón

**Archivo:** `src/components/InvalidConfigDialog.tsx:134`

**El bug:** Usar un executor `async` dentro de `new Promise()` es un error conocido. Si la función async lanza una excepción, la Promise **nunca se resuelve ni rechaza** — el programa queda colgado.

```typescript
// BUG en el original:
await new Promise<void>(async resolve => {
    const { unmount } = await render(<DialogComponent ... />)
    // Si render() falla aquí, la Promise cuelga para siempre
})
```

**Equivalente Python que hay que evitar:**
```python
# MAL
async def operacion_colgante():
    resultado = asyncio.Future()
    async def executor():
        await hacer_algo()  # Si falla, el Future nunca se completa
        resultado.set_result(None)
    asyncio.create_task(executor())  # Si executor() lanza, Future cuelga
    await resultado

# BIEN para Claw
async def operacion_segura():
    await hacer_algo()  # Directamente await, o envolver en try/except
```

---

### BUG #6 — Fire-and-forget sin `.catch()` en plans.ts

**Archivo:** `src/utils/plans.ts:184`

El propio código tiene un comentario que documenta el bug:
```typescript
// Don't throw — called fire-and-forget (void copyPlanForResume(...)) with no .catch()
```

Esto significa que si `copyPlanForResume()` falla (ej: disco lleno), el error desaparece completamente. Para Claw, la **memoria automática** (Fase 1) debe manejar esto correctamente:

```python
# MAL - fire-and-forget sin manejo de errores
asyncio.create_task(guardar_memoria())  # Errores silenciados

# BIEN para la memoria automática de Claw
async def guardar_memoria_seguro():
    try:
        await guardar_memoria()
    except OSError as e:
        logger.error(f"Error al guardar memoria: {e}")
        # Notificar al usuario si es crítico
    except Exception as e:
        logger.warning(f"Error inesperado en memoria: {e}")

asyncio.create_task(guardar_memoria_seguro())
```

---

### BUG #7 — `get3PModelCapabilityOverride` está memoizado pero lee `os.environ`

**Archivo:** `src/utils/model/modelSupportOverrides.ts`

```typescript
export const get3PModelCapabilityOverride = memoize(
  (model: string, capability: ModelCapabilityOverride) => {
    // Lee process.env aquí
    const pinned = process.env[tier.modelEnvVar]  // Variable de entorno
    // ...
  },
  (model, capability) => `${model.toLowerCase()}:${capability}`  // Cache key
)
```

**El bug:** La función lee variables de entorno pero está cacheada. Si el usuario cambia las variables en runtime (raro pero posible), el cache devuelve valores obsoletos.

**Para Claw:** No cachear funciones que leen `os.environ` a menos que el caché se invalide correctamente:

```python
# MAL
@functools.lru_cache(maxsize=None)
def tiene_capacidad_thinking(modelo: str) -> bool:
    env_var = os.environ.get('MODELO_CAPACIDADES', '')  # Lee env - NUNCA cachear así
    return 'thinking' in env_var

# BIEN
def tiene_capacidad_thinking(modelo: str) -> bool:
    # Sin caché, o caché invalidable por evento
    env_var = os.environ.get('MODELO_CAPACIDADES', '')
    return 'thinking' in env_var
```

---

## 🟢 BUGS MENORES / PATRONES A EVITAR

---

### BUG #8 — Race condition en useEffect sin cleanup

**Múltiples archivos** (`useReplBridge.tsx`, `useInboxPoller.ts`, etc.)

Patrón repetido: `void (async () => { ... })()` dentro de hooks de React sin función de cleanup. Si el componente se desmonta antes de que el async termine, puede actualizar estado en un componente ya destruido.

**Para Claw (Fase 2, Voz):** En el pipeline de Whisper, usar un flag de cancelación:

```python
import asyncio

class PipelineVoz:
    def __init__(self):
        self._cancelado = False
        
    async def grabar_y_transcribir(self):
        self._cancelado = False
        try:
            audio = await self._grabar()
            if self._cancelado:
                return None
            texto = await self._transcribir(audio)
            if self._cancelado:
                return None
            return texto
        except asyncio.CancelledError:
            logger.info("Pipeline de voz cancelado")
            return None
    
    def cancelar(self):
        self._cancelado = True
```

---

### BUG #9 — `parseInt()` sin validación de NaN

**Archivo:** `src/utils/thinking.ts:148`

```typescript
return parseInt(process.env.MAX_THINKING_TOKENS, 10) > 0
// Si MAX_THINKING_TOKENS="abc", parseInt devuelve NaN
// NaN > 0 es false, pero no por la razón correcta
```

**Para Claw:**
```python
def obtener_max_thinking_tokens() -> int:
    raw = os.environ.get('MAX_THINKING_TOKENS', '')
    try:
        valor = int(raw)
        if valor < 0:
            raise ValueError("Debe ser positivo")
        return valor
    except (ValueError, TypeError):
        return 8000  # Default seguro
```

---

### BUG #10 — Regex con `/g` compartida entre llamadas (regex state leak)

**Archivo:** `src/utils/thinking.ts:45`

El propio código tiene un comentario explicando el bug que corrigieron:
```typescript
// Fresh /g literal each call — String.prototype.matchAll copies lastIndex
// from the source regex, so a shared instance would leak state from
// hasUltrathinkKeyword's .test() into this call on the next render.
const matches = text.matchAll(/\bultrathink\b/gi)  // <- Literal nuevo cada vez
```

**Para Claw (si usa re module de Python):** `re.compile()` es seguro para reutilizar en Python porque `re.findall()` / `re.finditer()` no tienen estado de lastIndex. No hay equivalente de este bug en Python estándar.

---

### BUG #11 — `void onCwdChangedForHooks()` sin catch en Shell.ts

**Archivo:** `src/utils/Shell.ts:402`

```typescript
void onCwdChangedForHooks(cwd, newCwd)
// Si onCwdChangedForHooks() falla, el error desaparece
```

Para Claw, los **hooks de directorio** deben ser seguros:

```python
async def notificar_cambio_directorio(dir_anterior: str, dir_nuevo: str):
    try:
        await ejecutar_hooks_directorio(dir_anterior, dir_nuevo)
    except Exception as e:
        logger.warning(f"Hook de directorio falló: {e}")
        # No propagar - el cambio de directorio fue exitoso
```

---

### BUG #12 — Thinking blocks en mensajes reproducidos causan error de API

**Archivo:** `src/query.ts:714-715`

```typescript
// These partial messages (especially thinking blocks) have invalid signatures
// that would cause "thinking blocks cannot be modified" API errors.
```

Cuando se reproducen mensajes de una sesión anterior, los bloques de thinking tienen firmas que la API verifica. Reproducirlos directamente causa error `400`.

**Para Claw (memoria persistente + multi-sesión):**
```python
def limpiar_mensajes_para_replay(mensajes: list) -> list:
    """
    Al cargar historial de sesión anterior, eliminar bloques de thinking
    que causarían errores de firma de API.
    """
    mensajes_limpios = []
    for msg in mensajes:
        if msg.get('role') == 'assistant':
            contenido_limpio = [
                bloque for bloque in msg.get('content', [])
                if bloque.get('type') not in ('thinking', 'redacted_thinking')
            ]
            if contenido_limpio:
                mensajes_limpios.append({**msg, 'content': contenido_limpio})
        else:
            mensajes_limpios.append(msg)
    return mensajes_limpios
```

---

## 📋 TABLA RESUMEN — Prioridades para Claw

| # | Bug | Severidad | Fase afectada | Acción |
|---|-----|-----------|---------------|--------|
| 1 | `catch {}` vacío / `bare except: pass` | 🔴 Crítico | Todas | Ya corregido parcialmente, continuar |
| 2 | UTF-8 Windows + chcp 65001 | 🔴 Crítico | Fase 1 (.bat) | Agregar al lanzador .bat y al inicio de claw.py |
| 3 | Qwen3 thinking no verificado | 🔴 Crítico | Actual | Verificar capacidades antes de enviar thinking |
| 4 | Thinking blocks en replay | 🟡 Alto | Fase 1 (memoria) | Filtrar thinking del historial guardado |
| 5 | Fire-and-forget sin catch | 🟡 Alto | Fase 1 (memoria auto) | Envolver en función segura |
| 6 | `new Promise(async =>)` anti-patrón | 🟡 Alto | Fase 2 (voz) | Usar await directo |
| 7 | Memoize + env vars | 🟢 Menor | Config | No cachear lecturas de os.environ |
| 8 | Race condition async sin cleanup | 🟢 Menor | Fase 2 (voz) | Usar flag de cancelación |
| 9 | parseInt sin validar NaN | 🟢 Menor | Config | int() con try/except |
| 10 | Regex /g state leak | 🟢 Info | N/A en Python | No aplica en Python |
| 11 | Hooks de directorio sin catch | 🟢 Menor | Bash tool | Envolver en try/except |
| 12 | Capacidades 3P no detectadas | 🟡 Alto | Qwen/terceros | Leer ANTHROPIC_*_CAPABILITIES |

---

## 🚀 PRÓXIMOS PASOS RECOMENDADOS

**Esta semana (Fase 1):**

1. Agregar al `.bat`:
   ```batch
   @echo off
   chcp 65001 > nul
   python claw.py %*
   ```

2. Agregar al inicio de `claw.py`:
   ```python
   if sys.platform == 'win32':
       sys.stdout.reconfigure(encoding='utf-8', errors='replace')
       sys.stderr.reconfigure(encoding='utf-8', errors='replace')
   ```

3. Para la memoria automática, usar el patrón de `guardar_memoria_seguro()` (Bug #6).

4. Para Qwen3, verificar capacidades antes de enviar thinking (Bug #3).

**Fases 2-4:** Los bugs #6, #8 son relevantes cuando implementes voz (Whisper) y Telegram.

---

*Análisis generado a partir del repositorio `collection-claude-code-source-code-main` — Mayo 2026*
