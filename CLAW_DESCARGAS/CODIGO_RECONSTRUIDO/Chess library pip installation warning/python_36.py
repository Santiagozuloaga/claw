@app.route('/make_move', methods=['POST'])
def make_move():
    # 1. Recibe movimiento del usuario (ej: "e2e4")
    # 2. Valida que sea legal
    # 3. Lo aplica al tablero
    # 4. La IA calcula su respuesta
    # 5. Retorna ambos movimientos + nuevo estado del tablero