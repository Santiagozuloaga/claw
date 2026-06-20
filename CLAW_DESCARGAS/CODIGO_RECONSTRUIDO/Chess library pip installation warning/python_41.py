if piece_at_source and piece_at_source.piece_type == chess.PAWN:
    if (board.turn == chess.WHITE and target_rank == 7):
        move = chess.Move.from_uci(move_uci + 'q')  # Promoción a Reina