# Optimización de CLAW (ClawSpring) — Informe de Análisis

**Fecha:** 2026-06-24
**Versión:** 1.0
**Autor:** Jules

## 1. Identificación de Código Duplicado

Durante el análisis se identificó una redundancia crítica entre los núcleos del sistema:

*   **Archivos Duplicados:** `01_SRC/2024-06-19_CLAW_CORE_V01.py` y `01_SRC/2024-06-19_CLAW_CLAWSPRING_CORE_V01.py` son prácticamente idénticos en un 95%. La versión `CLAWSPRING_CORE` contiene correcciones adicionales para UTF-8 en Windows y mejor manejo de excepciones, mientras que `CORE_V01` incluye las reglas de seguridad física ISO-SAGE (`sage_check_cooling`).
*   **Módulos de Agent:** `01_SRC/2024-06-19_CLAW_AGENT_V01.py` y `01_SRC/2024-06-19_CLAW_AGENT_CORE_V01.py` son duplicados funcionales.

### Sugerencia:
Fusionar estos archivos en un único punto de entrada oficial para reducir la deuda técnica y evitar inconsistencias en el comportamiento del asistente.

## 2. Mejoras de Performance

### Carga Dinámica de Módulos (Imports)
Actualmente, el sistema utiliza `importlib.import_module` de forma extensiva (más de 30 ocurrencias de carga de `CONFIG_V01`). Aunque esto permite el uso de guiones en los nombres de archivos según ISO-SAGE, la carga repetitiva dentro de funciones:
1. Incrementa ligeramente la latencia de ejecución de comandos.
2. Dificulta el análisis estático de código.

**Recomendación:** Mover los imports de `importlib` al nivel de módulo (global) siempre que sea posible, en lugar de importarlos localmente dentro de cada función.

### Cálculo de Costos
Existen dos implementaciones de `calc_cost`: una en `PROVIDERS_V01` y otra en `CONFIG_V01`. El REPL (`CORE_V01`) importa la versión de `CONFIG_V01`.

**Recomendación:** Centralizar la lógica de costos en `PROVIDERS_V01` (donde reside el conocimiento de los modelos) y eliminar la duplicidad en el archivo de configuración.

## 3. Refactorizaciones Sugeridas

1.  **Unificación de Nombres:** Eliminar archivos `_CORE_` redundantes y mantener una única rama principal de ejecución.
2.  **Manejo de I/O:** Se ha detectado que `Path.read_text(newline="")` falla en el entorno actual. Se ha corregido usando `open().read()`, pero se sugiere crear una utilidad de sistema en `TOOLS_V01` para manejar lecturas/escrituras de archivos de forma consistente y segura entre versiones de Python.
3.  **Gestión de Estados:** El objeto `AgentState` se recrea con frecuencia. Considerar el uso de un gestor de contexto o un Singleton para la sesión activa para facilitar el acceso a la memoria desde cualquier módulo sin inyecciones manuales de `config`.

## 4. Estado de Nomenclatura ISO-SAGE

Se ha verificado que todos los archivos funcionales ahora siguen estrictamente el formato `[AAAA-MM-DD]_[PROYECTO]_[DESCRIPCIÓN]_V[XX].[ext]`. Las referencias internas han sido actualizadas para utilizar cargadores dinámicos que soportan los guiones en los nombres de los módulos.
