fetch('/get_board_state')
.then(r => r.json())
.then(data => {
    console.log(data.fen);
    console.log(data.legal_moves); // ["e2e4", "d2d4", ...]
});