import pytest
from src.app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_create_user(client):
    response = client.post('/graphql', json={
        'query': '''
        mutation {
            createUser(input: { username: "testuser", role: "student" }) {
                id
                username
                role
            }
        }
        '''
    })
    assert response.status_code == 200
    data = response.get_json()
    assert 'data' in data
    assert data['data']['createUser']['username'] == "testuser"

def test_update_user(client):
    response = client.post('/graphql', json={
        'query': '''
        mutation {
            updateUser(id: "1", input: { username: "updateduser" }) {
                id
                username
            }
        }
        '''
    })
    assert response.status_code == 200
    data = response.get_json()
    assert 'data' in data
    assert data['data']['updateUser']['username'] == "updateduser"

def test_delete_user(client):
    response = client.post('/graphql', json={
        'query': '''
        mutation {
            deleteUser(id: "1") {
                id
            }
        }
        '''
    })
    assert response.status_code == 200
    data = response.get_json()
    assert 'data' in data
    assert data['data']['deleteUser']['id'] == "1"

def test_list_users(client):
    response = client.post('/graphql', json={
        'query': '''
        query {
            users {
                id
                username
                role
            }
        }
        '''
    })
    assert response.status_code == 200
    data = response.get_json()
    assert 'data' in data
    assert isinstance(data['data']['users'], list)