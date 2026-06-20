fetch('/save_game', {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify({
        filename: 'mi_partida',
        overwrite: true
    })
});

// Response
{
    "status": "success",
    "filename": "mi_partida.pgn",
    "message": "Partida guardada como mi_partida.pgn"
}