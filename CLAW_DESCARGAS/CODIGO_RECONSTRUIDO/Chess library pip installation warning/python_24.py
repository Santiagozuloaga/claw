if (board.turn == chess.WHITE and chess.square_rank(move.to_square) == 7) or
   (board.turn == chess.BLACK and chess.square_rank(move.to_square) == 0):
    # Agregar promoción