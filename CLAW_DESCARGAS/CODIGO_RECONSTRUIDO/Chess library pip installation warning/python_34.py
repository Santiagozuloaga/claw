game_sessions: Dict[str, Dict[str, Any]] = {}

def get_or_create_session() -> str:
    if 'game_id' not in session:
        session['game_id'] = str(uuid.uuid4())