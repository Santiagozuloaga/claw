@app.route('/set_difficulty', methods=['POST'])
def set_difficulty():
    # Cambia la profundidad de búsqueda (1-5)
    # Profundidad 5 = IA muy fuerte (piensa 5 movimientos adelante)