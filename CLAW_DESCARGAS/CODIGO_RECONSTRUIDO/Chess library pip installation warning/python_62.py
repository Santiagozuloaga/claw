@app.route('/')
@session_required
def index():
    # Lee el archivo index.html desde la ubicación actual
    with open('index.html', 'r', encoding='utf-8') as f:
        return f.read(), 200