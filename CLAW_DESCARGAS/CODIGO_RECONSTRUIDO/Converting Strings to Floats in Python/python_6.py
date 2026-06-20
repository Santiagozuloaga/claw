jugadores = {}
for i in range(3):
    # Validación del nombre
    while True:
        nombre = input(f"Ingresa el nombre del jugador {i+1}: ").strip()
        if nombre and nombre not in jugadores:
            break
        print("Error: El nombre no puede estar vacío o ya existe")
    
    # Validación de goles
    while True:
        try:
            n_goles = int(input(f"Ingresa la cantidad de goles de {nombre}: "))
            if n_goles >= 0:
                break
            print("Error: Los goles no pueden ser negativos")
        except ValueError:
            print("Error: Debes ingresar un número válido")
    
    jugadores[nombre] = n_goles

print("\nEstadísticas de jugadores:")
for nombre, goles in jugadores.items():
    print(f"{nombre}: {goles} goles")