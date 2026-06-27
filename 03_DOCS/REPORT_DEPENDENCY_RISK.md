# MATRIZ DE RIESGO DE DEPENDENCIAS — CLAW (FASE 0)

Este informe clasifica los componentes por su riesgo para la estabilidad del repositorio.

## 1. Clasificación por Estado

| Módulo | Clasificación | Nivel de Riesgo | Razón |
| :--- | :--- | :--- | :--- |
| `run_claw.py` | ROTO | CRÍTICO | Referencia de import incorrecta. |
| `CORE_V01.py` | INESTABLE | CRÍTICO | Posee imports hacia archivos inexistentes. |
| `memory/` | ACTIVO | BAJO | Utilizado correctamente por múltiples archivos. |
| `task/` | ACTIVO | BAJO | Utilizado correctamente. |
| `mcp/` | ACTIVO | BAJO | Utilizado correctamente. |
| `2024-06-19_CLAW_.../` | HUÉRFANO | MEDIO | No se usan, pero ocupan espacio y causan confusión. |
| `SHIM_V01.py` | COMPATIBILIDAD | BAJO | Solo redirigen, riesgo de circularidad bajo. |

## 2. Acciones de Mitigación
1. **Consolidar el Core:** La prioridad absoluta es que el Core use nombres de archivos que existan físicamente.
2. **Eliminar Huérfanos:** Borrar las carpetas que empiezan por fecha (Fase A de limpieza) liberará el path de ruido.

## 3. Conclusión Final
El sistema es recuperable mediante cambios en las declaraciones de `import`. No se requiere reescribir lógica de negocio, solo "coser" (stitch) las referencias entre archivos y carpetas existentes.
