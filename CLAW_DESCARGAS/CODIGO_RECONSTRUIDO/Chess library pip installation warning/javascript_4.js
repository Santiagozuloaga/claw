// Debugging verbose
window.DEBUG = true;

function makeMove(move) {
  if (window.DEBUG) {
    console.log('%c📤 ENVIANDO MOVIMIENTO', 'color: blue; font-weight: bold');
    console.log('Move UCI:', move);
    console.log('isThinking:', isThinking);
  }
  // ... resto del código
}