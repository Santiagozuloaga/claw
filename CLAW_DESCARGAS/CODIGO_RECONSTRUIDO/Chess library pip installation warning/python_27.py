# ✅ Verificación más robusta
if piece_at_source and piece_at_source.piece_type == chess.PAWN:
    target_rank = chess.square_rank(move.to_square)
    if (board.turn == chess.WHITE and target_rank == 7) or \
       (board.turn == chess.BLACK and target_rank == 0):
        if not move.promotion:
            move = chess.Move.from_uci(move_uci + promotion_piece)