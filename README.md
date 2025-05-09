# Health Information System
A basic health information system to manage clients and health programs/services, built using Flask. This system allows a doctor (system user) to create health programs, register clients, enroll them in programs, and expose their profiles via an API.

Features
## Create Health Program: Add programs such as TB, Malaria, HIV, etc.

## Register Clients: Add new clients with basic information.

## Enroll Clients in Programs: Assign clients to one or more health programs.

## Search for Clients: Search for clients by name.

## View Client Profile: View the profile of a client along with the programs they are enrolled in.

## Expose Client Profile via API: Access client profiles via an API to integrate with other systems.

# Technologies Used
### Backend: Flask (Python)

### Testing: pytest

### API: RESTful APIs

### Data format: JSON

### Database: In-memory data storage (For this task, it could be a simple dictionary or a small database depending on your choice)

# Setup Instructions
## Prerequisites
### Make sure you have the following installed on your machine:

Python 3.x

pip (Python package installer)

Installation Steps
Clone the repository:

git clone https://github.com/your-username/health-info-system.git
cd health-info-system
Install the required dependencies:

pip install -r requirements.txt
Run the Flask application:

python app.py
The application will start running on http://127.0.0.1:5000/.

## Access the API endpoints:

#### POST /programs: Create a new health program.

#### POST /clients: Register a new client.

#### POST /clients/enroll: Enroll a client in one or more programs.

#### GET /clients/search?query=Alice: Search for clients by name.

#### GET /clients/{client_id}: View a client's profile.

## Testing
#### To run the tests for this application, use pytest:

pytest
The tests are located in the test_app.py file.

# API Documentation
### Here is a list of available API endpoints:

#### POST /programs
Create a new health program.

{
  "name": "TB Program",
  "description": "Treatment for Tuberculosis"
}

{
  "message": "Program created",
  "program_id": 1
}
#### POST /clients
Register a new client.

{
  "name": "Alice",
  "age": 28
}

{
  "message": "Client registered",
  "client_id": 1
}
#### POST /clients/enroll
Enroll a client in one or more programs.
{
  "client_id": 1,
  "program_ids": [1]
}
{
  "message": "Client enrolled in programs"
}
#### GET /clients/search?query=Alice
Search for a client by name.

{
  "1": {
    "name": "Alice",
    "age": 28
  }
}
#### GET /clients/{client_id}
View a client's profile.
{
  "client": {
    "name": "Alice",
    "age": 28
  },
  "programs": [
    {
      "name": "TB Program",
      "description": "Treatment for Tuberculosis"
    }
  ]
}
