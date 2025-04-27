import json
import pytest
from app import app

@pytest.fixture
def client():
    """Fixture for setting up a test client."""
    with app.test_client() as client:
        yield client

def test_create_program(client):
    """Test creating a new program."""
    program_data = {"name": "TB Program", "description": "Treatment for Tuberculosis"}
    response = client.post('/programs', json=program_data)
    data = json.loads(response.data)

    assert response.status_code == 200
    assert data['message'] == "Program created"
    assert 'program_id' in data

def test_register_client(client):
    """Test registering a new client."""
    client_data = {"name": "Alice", "age": 28}
    response = client.post('/clients', json=client_data)
    data = json.loads(response.data)

    assert response.status_code == 200
    assert data['message'] == "Client registered"
    assert 'client_id' in data

def test_enroll_client(client):
    """Test enrolling a client in a program."""
    # First, create a program
    program_data = {"name": "TB Program", "description": "Treatment for Tuberculosis"}
    response = client.post('/programs', json=program_data)
    program_id = json.loads(response.data)['program_id']

    # Now, register a client
    client_data = {"name": "Alice", "age": 28}
    response = client.post('/clients', json=client_data)
    client_id = json.loads(response.data)['client_id']

    # Enroll the client in the program
    enrollment_data = {"client_id": client_id, "program_ids": [program_id]}
    response = client.post('/clients/enroll', json=enrollment_data)
    data = json.loads(response.data)

    assert response.status_code == 200
    assert data['message'] == "Client enrolled in programs"

def test_search_client(client):
    """Test searching for a client by name."""
    # Register a new client
    client_data = {"name": "Alice", "age": 28}
    client.post('/clients', json=client_data)

    # Search for the client by name
    response = client.get('/clients/search?query=Alice')
    data = json.loads(response.data)

    assert response.status_code == 200
    # Check if client data is in the response
    assert any(client['name'] == "Alice" and client['age'] == 28 for client in data.values())

def test_view_client_profile(client):
    """Test viewing a client's profile."""
    # Register a new client
    client_data = {"name": "Alice", "age": 28}
    response = client.post('/clients', json=client_data)
    client_id = json.loads(response.data)['client_id']

    # Create a program
    program_data = {"name": "TB Program", "description": "Treatment for Tuberculosis"}
    response = client.post('/programs', json=program_data)
    program_id = json.loads(response.data)['program_id']

    # Enroll the client in the program
    enrollment_data = {"client_id": client_id, "program_ids": [program_id]}
    client.post('/clients/enroll', json=enrollment_data)

    # View the client's profile
    response = client.get(f'/clients/{client_id}')
    data = json.loads(response.data)

    assert response.status_code == 200
    assert 'client' in data
    assert data['client']['name'] == "Alice"
    assert len(data['programs']) == 1  # The client should be enrolled in one program

def test_expose_client_profile(client):
    """Test exposing a client's profile via API."""
    # Register a new client
    client_data = {"name": "Alice", "age": 28}
    response = client.post('/clients', json=client_data)
    client_id = json.loads(response.data)['client_id']

    # Create a program
    program_data = {"name": "TB Program", "description": "Treatment for Tuberculosis"}
    response = client.post('/programs', json=program_data)
    program_id = json.loads(response.data)['program_id']

    # Enroll the client in the program
    enrollment_data = {"client_id": client_id, "program_ids": [program_id]}
    client.post('/clients/enroll', json=enrollment_data)

    # Expose the client's profile via the API
    response = client.get(f'/clients/{client_id}')
    data = json.loads(response.data)

    assert response.status_code == 200
    assert data['client']['name'] == "Alice"
    assert len(data['programs']) == 1

