from flask import Blueprint, request, jsonify
from programs import programs  # Import the programs dictionary from programs.py

client_routes = Blueprint('client_routes', __name__)

# Store clients with unique IDs
clients = {}

@client_routes.route('', methods=['POST'])
def register_client():
    """Register a new client in the system."""
    try:
        client_data = request.json
        if not client_data or 'name' not in client_data or 'age' not in client_data:
            return jsonify({"message": "Missing required fields: 'name' or 'age'"}), 400
        
        client_id = len(clients) + 1
        clients[client_id] = client_data
        return jsonify({"message": "Client registered", "client_id": client_id})
    
    except Exception as e:
        return jsonify({"message": str(e)}), 500

@client_routes.route('/enroll', methods=['POST'])
def enroll_client():
    """Enroll a client in one or more programs."""
    try:
        enrollment_data = request.json
        client_id = enrollment_data['client_id']
        program_ids = enrollment_data['program_ids']
        
        if client_id not in clients:
            return jsonify({"message": "Client not found"}), 404
        
        # Enroll the client in the provided programs
        if 'programs' not in clients[client_id]:
            clients[client_id]['programs'] = []
        
        for program_id in program_ids:
            if program_id not in programs:
                return jsonify({"message": f"Program {program_id} not found"}), 404
            if program_id not in clients[client_id]['programs']:
                clients[client_id]['programs'].append(program_id)
        
        return jsonify({"message": "Client enrolled in programs"})
    
    except Exception as e:
        return jsonify({"message": str(e)}), 500

@client_routes.route('/search', methods=['GET'])
def search_clients():
    """Search for a client by name."""
    query = request.args.get('query')
    result = {client_id: client for client_id, client in clients.items() if query.lower() in client['name'].lower()}
    return jsonify(result)

@client_routes.route('/<int:client_id>', methods=['GET'])
def view_client(client_id):
    """View a client's profile, including programs they are enrolled in."""
    client = clients.get(client_id)
    if client:
        enrolled_programs = [programs[program_id] for program_id in client.get('programs', [])]
        return jsonify({"client": client, "programs": enrolled_programs})
    else:
        return jsonify({"message": "Client not found"}), 404
