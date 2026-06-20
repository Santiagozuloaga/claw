# ✅ Funciones de 10-15 líneas máximo
# Responsabilidad única (SRP)
def get_piece_value(letter: str) -> int:
    return PIECE_VALUES.get(letter, 0)