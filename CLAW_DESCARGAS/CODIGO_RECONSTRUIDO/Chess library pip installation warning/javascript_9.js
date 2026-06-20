function updateStatus(message, type) {
  const $status = $('#status');
  $status.text(message);
  $status.removeClass('error thinking success gameover');
  if (type) {
    $status.addClass(type);
  }
}