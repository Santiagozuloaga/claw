function onDrop(source, target) {
  const move = source + target; // ✅ Solo construye UCI
  makeMove(move);               // ✅ Envía al servidor
  return 'snapback';            // ✅ Tablero se actualiza con FEN del servidor
}