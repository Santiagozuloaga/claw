if board.is_game_over():
    return jsonify({
        'status': 'game_over',
        'message': f'¡Fin del juego! Resultado: {board.result()}'
    })