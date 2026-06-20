function onDrop(source, target) {
    if (isThinking) {
        return 'snapback'; // Evitar movimientos durante el turno de la IA
    }
    
    const move = source + target; // Formato UCI: "e2e4"
    makeMove(move); // Enviar al backend
    
    return 'snapback'; // La pieza vuelve hasta que el servidor confirme
}