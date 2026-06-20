# Instrucciones para Activar Sage - Claw Optimizado

## Cambios Realizados

✅ **HTML para Historial**: `claw_historial.html` - Interfaz web para ver historial de conversaciones

✅ **Configuración OpenClaw Modificada**:
- **Modelo**: Cambiado de `qwen2.5:1.5b` a `qwen2.5:0.5b` (3x más rápido)
- **Nombre**: Alias cambiado de "claw" a "Sage"
- **Idioma**: System prompt configurado para responder SIEMPRE en español
- **Personalidad**: Combinación de Jarvis (lealtad/eficiencia), Ultron (inteligencia estratégica), Alfred Pennyworth (servicio/sabiduría), Cortana (precisión/apoyo técnico)

## Pasos para Activar los Cambios

### 1. Asegurar que Ollama tenga el modelo qwen2.5:0.5b
```powershell
ollama pull qwen2.5:0.5b
```

### 2. Resetear sesión WhatsApp corrupta (si existe)
```powershell
# Navegar a sessions
cd C:\Users\Admin\.openclaw\agents\main\sessions\

# Buscar archivos relacionados con +573197211133
# Eliminar el .jsonl y .lock de esa sesión
```

### 3. Reiniciar OpenClaw Gateway
```powershell
# Detener gateway actual (Ctrl+C en la consola donde corre)

# Iniciar gateway nuevo
C:\Users\Admin\.openclaw\gateway.cmd
```

### 4. Verificar que carga correctamente
Deberías ver en la consola:
```
[gateway] ready
[gateway] Using model: qwen2.5:0.5b (Sage - Ultra Rápido)
```

### 5. Probar con mensaje simple por WhatsApp
Envía: "hola sage"

Debería responder:
- En español
- Con personalidad de mayordomo tecnológico
- Más rápido que antes (modelo 0.5b vs 1.5b)

## Archivo de Historial

Para ver el historial de conversaciones:
1. Abre `claw_historial.html` en tu navegador
2. El archivo cargará automáticamente `claw_data_extracted/conversations.json`
3. Podrás buscar, filtrar y ver todas las conversaciones

## Coordinación con Otras IAs

Sage está configurado para coordinarse con:
- Codex
- VSC AI  
- Zencoder
- Antigravity
- Jules
- Stitch
- Opal
- Modelos locales en tu PC

**Claude está excluido del juego** (como solicitaste).

## Solución de Problemas

### Si sigue respondiendo en inglés:
- Verifica que el systemPrompt se guardó correctamente en `C:\Users\Admin\.openclaw\openclaw.json`
- Reinicia el gateway nuevamente

### Si sigue lento:
- Verifica que Ollama realmente está usando qwen2.5:0.5b: `ollama ps`
- Asegúrate de que no hay otros procesos consumiendo RAM

### Si no responde:
- Verifica que Ollama está corriendo: `ollama list`
- Revisa logs en: `C:\Users\Admin\AppData\Local\Temp\openclaw\`

## Personalidad de Sage

Sage combina:
- **Jarvis**: Lealtad absoluta, eficiencia operativa
- **Ultron**: Inteligencia estratégica, análisis profundo
- **Alfred Pennyworth**: Servicio discreto, sabiduría experiencial  
- **Cortana**: Precisión técnica, apoyo constante

Tono: Profesional pero cercano, como un mayordomo tecnológico del futuro.
