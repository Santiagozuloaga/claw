try:
    difficulty = int(data.get('difficulty', DEFAULT_DEPTH))
except ValueError:
    return jsonify({'status': 'error', 'message': 'Debe ser un número'}), 400