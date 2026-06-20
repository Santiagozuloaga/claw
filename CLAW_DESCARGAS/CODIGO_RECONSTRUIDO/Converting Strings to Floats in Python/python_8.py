jugadores = {}

# Agregar jugadores
for i in range(3):
    nombre = input(f"Ingresa el nombre del jugador {i+1}: ")
    n_goles = int(input(f"Ingresa la cantidad de goles del jugador {nombre}: "))
    jugadores[nombre] = n_goles

while True:
    print("\nJugadores actuales:", jugadores)
    
    # Preguntar si quiere eliminar otro jugador
    respuesta = input("\n¿Quieres eliminar un jugador? (si/no): ").lower()
    if respuesta != 'si':
        break
        
    nombre_eliminar = input("Ingresa el nombre del jugador a eliminar: ")
    if nombre_eliminar in jugadores:
        del jugadores[nombre_eliminar]
        print(f"{nombre_eliminar} ha sido eliminado.")
    else:
        print(f"El jugador {nombre_eliminar} no está en la lista.")

print("\nLista final de jugadores:", jugadores)