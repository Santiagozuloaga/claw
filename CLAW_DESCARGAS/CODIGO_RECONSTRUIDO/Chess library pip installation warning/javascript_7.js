function onDragStart(source, piece, position, orientation) {
  console.log('🎯 onDragStart:', source, piece);
  
  if (isThinking) {
    console.log('⏸️ Bloqueado: IA está pensando');
    updateStatus('⏳ Espera...', 'thinking');
    return false;
  }
  
  if (piece.search(/^b/) !== -1) {
    console.log('❌ No puedes mover negras');
    return false;
  }
  
  return true;
}