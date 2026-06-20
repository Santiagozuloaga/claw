# test_sessions.py
import requests
import concurrent.futures

def test_session(session_id):
    with requests.Session() as s:
        # Cada sesión mantiene sus propias cookies
        r = s.post('http://localhost:5000/make_move', 
                   json={'move': 'e2e4'})
        print(f"Sesión {session_id}: {r.status_code}")

# Simular 10 usuarios concurrentes
with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
    executor.map(test_session, range(10))