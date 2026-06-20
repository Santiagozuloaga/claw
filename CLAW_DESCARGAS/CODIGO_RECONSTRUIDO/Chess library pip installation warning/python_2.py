# Cada usuario tiene su propio estado de juego
game_sessions = {
    'uuid-1234': {'board': chess.Board(), 'depth': 3},
    'uuid-5678': {'board': chess.Board(), 'depth': 5},
}

# Flask sessions identifica a cada usuario
session['game_id'] = str(uuid.uuid4())