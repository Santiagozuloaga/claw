# REPORTE DE PUNTO DE ENTRADA Y RUNTIME — CLAW (FASE 0)

Este informe detalla exactamente qué sucede al iniciar el sistema.

## 1. Análisis de run_claw.py
El archivo raíz es el lanzador oficial. Su lógica es:
1. Agrega `01_SRC` y `00_SOPORTE` al path.
2. Intenta: `importlib.import_module("CLAW_2024_06_19_CORE_V01")`.

**FALLO DETECTADO:** El archivo físico se llama `2024-06-19_CLAW_CORE_V01.py`. El sistema busca el nombre invertido y falla.

## 2. Módulos Cargados al Iniciar (Teórico)
Si el Core iniciara correctamente, estos serían los módulos cargados en los primeros 100ms:
* `2024-06-19_CLAW_PROVIDERS_V01` (Como 'PROVIDERS')
* `2024-06-19_CLAW_CONFIG_V01` (Desde 00_SOPORTE)
* `memory/` (Paquete físico)
* `task/` (Paquete físico)
* `mcp/` (Paquete físico)

## 3. Bootstrap
El bootstrap está roto en la raíz. Ningún agente puede ejecutar el proyecto sin modificar manualmente `run_claw.py` o renombrar el Core.

## 4. Recomendación Crítica
La primera acción de recuperación DEBE ser corregir la cadena de importación en `run_claw.py`. Sin esto, no es posible verificar funcionalmente ninguna otra reparación.
