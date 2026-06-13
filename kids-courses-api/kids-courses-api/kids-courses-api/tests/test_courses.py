import pytest
from strawberry.test import Client
from src.app import schema

@pytest.fixture
def client():
    return Client(schema)

def test_list_courses(client):
    query = "{ listCourses { id title description } }"
    response = client.execute(query)
    assert "data" in response
    assert "listCourses" in response["data"]

def test_create_course(client):
    mutation = """
    mutation {
        createCourse(title: "New Course", description: "Course Description") {
            id
            title
            description
        }
    }
    """
    response = client.execute(mutation)
    assert "data" in response
    assert "createCourse" in response["data"]
    assert response["data"]["createCourse"]["title"] == "New Course"

def test_update_course(client):
    mutation = """
    mutation {
        updateCourse(id: "1", title: "Updated Course", description: "Updated Description") {
            id
            title
            description
        }
    }
    """
    response = client.execute(mutation)
    assert "data" in response
    assert "updateCourse" in response["data"]
    assert response["data"]["updateCourse"]["title"] == "Updated Course"