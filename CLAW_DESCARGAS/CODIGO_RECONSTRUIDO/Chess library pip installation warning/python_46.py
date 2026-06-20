# ❌ MAL: f-string sin variables
mensaje = f"Hola mundo"
print(f"El juego terminó")

# ✅ BIEN: String normal
mensaje = "Hola mundo"
print("El juego terminó")

# ✅ BIEN: f-string CON variables
nombre = "Carlos"
mensaje = f"Hola {nombre}"
resultado = "1-0"
print(f"El juego terminó: {resultado}")