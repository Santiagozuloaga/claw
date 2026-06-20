# f-string CON placeholder (correcto)
nombre = "Juan"
mensaje = f"Hola {nombre}"  # ✅ Tiene {nombre}

# f-string SIN placeholder (warning)
mensaje = f"Hola mundo"     # ⚠️ No necesita f, es solo texto