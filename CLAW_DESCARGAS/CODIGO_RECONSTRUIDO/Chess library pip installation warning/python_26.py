# ❌ ANTES (incorrecto)
board.piece_at(move.from_square) == chess.Piece(chess.PAWN, board.turn)

# ✅ DESPUÉS (correcto)
piece_at_source = board.piece_at(move.from_square)
if piece_at_source and piece_at_source.piece_type == chess.PAWN: