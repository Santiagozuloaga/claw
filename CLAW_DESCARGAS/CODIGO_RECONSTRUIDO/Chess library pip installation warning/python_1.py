@app.route('/new_game', methods=['POST'])
def new_game():
    global board
    board.reset()
    return jsonify({
        'fen': board.fen(),
        'status': 'Nueva partida iniciada'
    })