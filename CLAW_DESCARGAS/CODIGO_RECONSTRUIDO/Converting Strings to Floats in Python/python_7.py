jugadores = {}

# Agregar jugadores
for i in range(3):
    nombre = input(f"Ingresa el nombre del jugador {i+1}: ")
    n_goles = int(input(f"Ingresa la cantidad de goles del jugador {nombre}: "))
    jugadores[nombre] = n_goles

print("\nJugadores actuales:", jugadores)

# Eliminar jugador
nombre_eliminar = input("\nIngresa el nombre del jugador que deseas eliminar: ")
if nombre_eliminar in jugadores:
    del jugadores[nombre_eliminar]
    print(f"\n{nombre_eliminar} ha sido eliminado.")
    print("Jugadores restantes:", jugadores)
else:
    print(f"\nEl jugador {nombre_eliminar} no está en la lista.")