jugadores = {}
for i in range(3):
    # Validación del nombre
    while True:
        nombre = input(f"Ingresa el nombre del jugador {i+1}: ").strip()
        if nombre:  # Verifica que no esté vacío
            break
        print("El nombre no puede estar vacío.")
    
    # Validación de goles
    while True:
        try:
            n_goles = int(input(f"Ingresa la cantidad de goles de {nombre}: "))
            if n_goles >= 0:  # Verifica que no sea negativo
                break
            print("El número de goles no puede ser negativo.")
        except ValueError:
            print("Por favor, ingresa un número válido.")
    
    jugadores[nombre] = n_goles

print("\nEstadísticas de jugadores:")
for jugador, goles in jugadores.items():
    print(f"{jugador}: {goles} goles")