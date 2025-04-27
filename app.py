from flask import Flask, send_from_directory
from programs import program_routes
from clients import client_routes
import os

app = Flask(__name__)

# Register blueprints for programs and clients
app.register_blueprint(program_routes, url_prefix='/programs')
app.register_blueprint(client_routes, url_prefix='/clients')

# Serve the front-end from the 'frontend' folder
@app.route('/')
def index():
    """Serves the homepage (index.html)."""
    return send_from_directory(os.path.join(app.root_path, 'frontend'), 'index.html')

# Serve static files (CSS, JS)
@app.route('/<path:path>')
def static_file(path):
    """Serves static files (CSS, JS) from the 'frontend' folder."""
    return send_from_directory(os.path.join(app.root_path, 'frontend'), path)

if __name__ == '__main__':
    app.run(debug=True)
