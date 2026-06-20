function makeMove(move) {
  isThinking = true;
  updateStatus('🤔 Procesando tu movimiento...', 'thinking');
  
  $.ajax({
    url: '/make_move',
    method: 'POST',
    contentType: 'application/json',
    data: JSON.stringify({ move: move, promotion: 'q' }),
    success: function(response) {
      if (response.status === 'error') {
        updateStatus('❌ ' + response.message, 'error');
        isThinking = false;
        return;
      }
      // Procesamiento directo...
    },
    error: function(xhr) {
      let errorMsg = 'Error de comunicación';
      try { errorMsg = JSON.parse(xhr.responseText).message; } catch(e) {}
      updateStatus('❌ ' + errorMsg, 'error');
      isThinking = false;
    }
  });
}