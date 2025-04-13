import pytest
from app import create_app, db

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'

    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client

def test_add_patient(client):
    response = client.post('/patients', json={'name': 'Ana', 'email': 'ana@test.com'})
    assert response.status_code == 200
    assert b'Patient added successfully' in response.data
