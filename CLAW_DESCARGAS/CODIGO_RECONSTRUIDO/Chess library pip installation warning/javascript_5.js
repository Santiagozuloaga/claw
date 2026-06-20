function makeMove(move) {
  isThinking = true;
  updateStatus('🤔 Procesando tu movimiento...', 'thinking');
  
  console.log('🌐 Enviando a /make_move:', move);
  
  $.ajax({
    url: '/make_move',
    method: 'POST',
    contentType: 'application/json',
    data: JSON.stringify({ move: move, promotion: 'q' }),
    success: function(response) {
      console.log('✅ Respuesta recibida:', response);
      handleMoveResponse(response);
    },
    error: function(xhr) {
      console.error('❌ Error AJAX:', xhr);
      // ... 10 líneas más
    }
  });
}