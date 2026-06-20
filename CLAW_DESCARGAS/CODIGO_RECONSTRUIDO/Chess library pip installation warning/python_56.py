def evaluate_board(board):
    evaluation = 0.0
    for square in chess.SQUARES:
        piece = board.piece_at(square)
        if piece:
            # Valor material
            evaluation += get_piece_value(piece)
            # ✨ NUEVO: Valor posicional (PST)
            evaluation += get_pst_value(piece, square, board)
    return evaluation