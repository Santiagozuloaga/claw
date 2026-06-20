// Validar sin aplicar permanentemente
const testMove = game.move({ from, to, promotion: 'q' });
if (testMove === null) return 'snapback';

// CRÍTICO: Revertir de inmediato
game.undo();

// Decidir si mostrar modal o enviar
if (willPromote) {
  showPromotionModal();
  return 'snapback';
}
sendMoveToServer(source + target, 'q');