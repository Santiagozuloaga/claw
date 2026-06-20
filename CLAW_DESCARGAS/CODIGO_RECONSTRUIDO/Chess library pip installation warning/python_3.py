MAX_SEARCH_TIME = 25  # segundos

def minimax(boardCopy, depth, alpha, beta, maximizingPlayer, start_time):
    if time.time() - start_time > MAX_SEARCH_TIME:
        return evaluateBoard(boardCopy)  # Retorna evaluación actual
    # ... resto del código