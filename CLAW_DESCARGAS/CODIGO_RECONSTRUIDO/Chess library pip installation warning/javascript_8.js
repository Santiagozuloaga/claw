function onDragStart(source, piece) {
  if (isThinking) {
    updateStatus('⏳ Espera a que la IA termine...', 'thinking');
    return false;
  }
  return piece.search(/^b/) === -1;
}