def save_game(board, game_config, filename, overwrite=False):
    # Guarda PGN (notación estándar)
    pgn_path = Path(PGN_FOLDER) / f"{filename}.pgn"
    game = chess.pgn.Game.from_board(board)
    
    # Guarda metadata JSON
    metadata = {
        'vs_machine': True,
        'level': 3,
        'elo': 1400,
        'created_at': '[REDACTED_INFRASTRUCTURE] 15:30:00',
        'moves_count': 25,
        'result': '1-0'
    }