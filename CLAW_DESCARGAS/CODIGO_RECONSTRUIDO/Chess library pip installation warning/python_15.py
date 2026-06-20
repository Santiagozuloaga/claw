# ❌ Antes: Loop tradicional
value = 0
for i in range(64):
    piece = board.piece_at(i)
    if piece:
        value += get_piece_value(piece.symbol())

# ✅ Después: Comprehension
return sum(
    get_piece_value(board.piece_at(i).symbol())
    for i in range(64)
    if board.piece_at(i)
)