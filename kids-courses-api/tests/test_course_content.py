import pytest
from strawberry.test import Client

from src.schema import schema
from src.resolvers import course_content


class FakeCollection:
    def __init__(self):
        self._documents = []
        self._counter = 1

    def find(self):
        return self

    async def to_list(self, length=None):
        return list(self._documents)

    async def insert_one(self, document):
        document["_id"] = self._counter
        self._counter += 1
        self._documents.append(document)
        return type("InsertResult", (), {"inserted_id": document["_id"]})()


class FakeDatabase:
    def __init__(self):
        self.course_content = FakeCollection()


@pytest.fixture
def client(monkeypatch):
    fake_db = FakeDatabase()
    monkeypatch.setattr(course_content, "get_database", lambda: fake_db)
    return Client(schema)


def test_create_course_content(client):
    mutation = """
    mutation {
        createCourseContent(
            courseRelatedId: "000000000000000000000001"
            description: "Lesson overview"
            content: "Line 1\nLine 2"
            weblink: "https://example.com"
            author: "Ada"
        ) {
            contentId
            courseRelatedId
            description
            content
            weblink
            author
        }
    }
    """

    response = client.execute(mutation)

    assert response["data"]["createCourseContent"]["content"] == "Line 1\nLine 2"
    assert response["data"]["createCourseContent"]["author"] == "Ada"
