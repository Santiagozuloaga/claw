function onDrop(source, target) {
  const move = game.move({ from: source, to: target }); // ❌ Valida localmente
  if (move === null) return 'snapback';
  // ... envía al servidor
}