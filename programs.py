from flask import Blueprint, request, jsonify

program_routes = Blueprint('program_routes', __name__)

# Store programs with unique IDs
programs = {}

@program_routes.route('', methods=['POST'])
def create_program():
    """Create a new health program (e.g., TB, Malaria, HIV)."""
    try:
        program_data = request.json
        if not program_data or 'name' not in program_data or 'description' not in program_data:
            return jsonify({"message": "Missing required fields: 'name' or 'description'"}), 400
        
        program_id = len(programs) + 1
        programs[program_id] = program_data
        return jsonify({"message": "Program created", "program_id": program_id})
    
    except Exception as e:
        return jsonify({"message": str(e)}), 500

@program_routes.route('/all', methods=['GET'])
def list_programs():
    """List all health programs."""
    return jsonify(programs)
