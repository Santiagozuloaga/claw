function updateStatus(message, type) {
  $('#status').text(message).removeClass('error thinking success gameover').addClass(type || '');
}