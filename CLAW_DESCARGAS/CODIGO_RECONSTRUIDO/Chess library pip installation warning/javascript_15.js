fetch('/list_games')
.then(r => r.json())
.then(data => {
    console.log(data.games);
    // [
    //   {filename: "partida1.pgn", elo: 1400, ...},
    //   {filename: "partida2.pgn", elo: 2000, ...}
    // ]
});