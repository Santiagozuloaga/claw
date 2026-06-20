def get_game_over_message(result):
    if result == "1-0":
        return "♚ ¡Las Blancas ganan!"
    elif result == "0-1":
        return "♚ ¡Las Negras ganan!"
    else:
        return "🤝 ¡Tablas!"