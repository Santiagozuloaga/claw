# INFORME DE CANONICALIZACIÓN DE MÓDULOS (FASE 0)

Este informe identifica qué versiones de los módulos duplicados son realmente utilizadas por el sistema CLAW.

## Resumen Ejecutivo
**HALLAZGO CRÍTICO:** Ninguna de las carpetas que empiezan por fecha (ej. `2024-06-19_CLAW_...`) es canónica ni funcionalmente activa. Python no permite importar carpetas cuyos nombres empiezan por números de forma directa. El sistema depende actualmente de las carpetas con nombres simples (`memory/`, `task/`, etc.).

---

## 1. Módulos Duplicados

### memory/
* **IMPORTADO POR:** `2024-06-19_CLAW_CORE_V01.py`, `2024-06-19_CLAW_MEMORY_SHIM_V01.py`, `context.py`.
* **ESTADO:** **ACTIVO**
* **VERSIÓN ISO:** `2024-06-19_CLAW_MEMORY_PACKAGE_V01/`
* **ESTADO ISO:** HUÉRFANO (Inimportable por nombre).
* **RECOMENDACIÓN:** Mantener `memory/`. Eliminar la carpeta ISO tras verificar que no hay lógica única en ella.
* **CONFIANZA:** ALTA

### task/
* **IMPORTADO POR:** `2024-06-19_CLAW_CORE_V01.py`, `2024-06-19_CLAW_TOOLS_V01.py`.
* **ESTADO:** **ACTIVO**
* **VERSIÓN ISO:** `2024-06-19_CLAW_TASK_V01/`
* **ESTADO ISO:** HUÉRFANO.
* **RECOMENDACIÓN:** Mantener `task/`.
* **CONFIANZA:** ALTA

### mcp/
* **IMPORTADO POR:** `2024-06-19_CLAW_CORE_V01.py`, `2024-06-19_CLAW_TOOLS_V01.py`.
* **ESTADO:** **ACTIVO**
* **VERSIÓN ISO:** `2024-06-19_CLAW_MCP_V01/`
* **ESTADO ISO:** HUÉRFANO.
* **RECOMENDACIÓN:** Mantener `mcp/`.
* **CONFIANZA:** ALTA

### skill/
* **IMPORTADO POR:** `2024-06-19_CLAW_CORE_V01.py`, `skills.py`, `2024-06-19_CLAW_SKILLS_SHIM_V01.py`.
* **ESTADO:** **ACTIVO**
* **VERSIÓN ISO:** `2024-06-19_CLAW_SKILL_V01/`
* **ESTADO ISO:** HUÉRFANO.
* **RECOMENDACIÓN:** Mantener `skill/`.
* **CONFIANZA:** ALTA

---

## 2. Evidencia Técnica
1. **Error de Sintaxis:** Ejecutar `import 2024-06-19_CLAW_...` produce un `SyntaxError` inmediato.
2. **Traceback de Core:** El Core (`2024-06-19_CLAW_CORE_V01.py`) tiene líneas como `from memory.scan import ...`. Si se eliminara `memory/`, el sistema colapsaría.
3. **Dualidad de Imports:** Muchos archivos ISO-SAGE internamente intentan importar usando nombres relativos (`from . import ...`), lo cual funcionaría si el paquete padre fuera importable, pero al no serlo desde el Core, quedan aislados.

---
**Conclusión:** La versión canónica funcional es la de **Nombres Simples**. La migración ISO-SAGE para carpetas falló por diseño de lenguaje.
