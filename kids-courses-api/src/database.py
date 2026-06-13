import os
from motor.motor_asyncio import AsyncIOMotorClient
from typing import Optional

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
MONGO_DB_NAME = os.getenv("MONGO_DB_NAME", "kids_courses_db")

_client: Optional[AsyncIOMotorClient] = None
_db = None

async def connect_to_mongo() -> None:
    global _client, _db
    if _client is None:
        _client = AsyncIOMotorClient(MONGO_URI)
        _db = _client[MONGO_DB_NAME]

async def disconnect_from_mongo() -> None:
    global _client
    if _client is not None:
        _client.close()
        _client = None


def get_database():
    if _db is None:
        raise RuntimeError("MongoDB is not connected. Call connect_to_mongo first.")
    return _db
