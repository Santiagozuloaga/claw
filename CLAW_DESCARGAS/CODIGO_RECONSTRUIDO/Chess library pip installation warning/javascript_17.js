// Al cambiar dificultad
$('#difficulty').change(function() {
  const level = parseInt($(this).val());
  
  $.ajax({
    url: '/set_difficulty',
    method: 'POST',
    contentType: 'application/json',
    data: JSON.stringify({ difficulty: level }),
    success: function(response) {
      if (response.status === 'success') {
        // Mostrar ELO equivalente
        updateStatus(`✅ Nivel ${response.level} (ELO ${response.elo}) configurado`, 'success');
      }
    }
  });
});