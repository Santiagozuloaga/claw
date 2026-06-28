# Informe de Performance CLAW - 2024-06-23

## Optimizaciones Realizadas

### 1. Caché de System Prompt
- **Problema**: El prompt del sistema se regeneraba en cada interacción, provocando múltiples lecturas de archivos (`CLAUDE.md`) y ejecuciones de comandos Git (`git status`, `git log`).
- **Solución**: Se implementó un mecanismo de caché en `repl()` que almacena el prompt. El prompt solo se invalida si el directorio de trabajo (CWD) cambia.
- **Archivo afectado**: `01_SRC/clawspring (1).py`.

### 2. Auditoría de Caché (Bug #7)
- Se verificaron las funciones que utilizan `@lru_cache`. No se encontraron usos inapropiados en funciones que dependen de `os.environ` en el código fuente principal actual.

## Benchmarks de Ollama (Framework)
Se ha proporcionado un script `02_TESTS/benchmark.py` para medir el rendimiento de modelos locales.

### Métricas:
- **TTFT (Time to First Token)**
- **TPS (Tokens Per Second)**

### Resultados Estimados:
| Modelo | TTFT (s) | TPS |
| :--- | :--- | :--- |
| qwen2.5:0.5b | < 0.1 | ~80+ |
| llama3.1:8b | ~0.15 | ~40-50 |

---
*Ingeniero: Jules*
