# ❌ ANTES (línea 607)
@app.route('/')
@session_required
def index():
    return render_template('index.html'), 200

# ✅ DESPUÉS
@app.route('/')
@session_required
def index():
    return app.send_static_file('index.html')