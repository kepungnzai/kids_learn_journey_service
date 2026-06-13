from typing import List, Optional
from bson import ObjectId
import strawberry
from ..database import get_database
from ..types import UserType

ALLOWED_USER_ROLES = {"student", "teacher", "admin"}


def _to_object_id(value: str) -> ObjectId:
    return ObjectId(str(value))


def _user_from_document(doc: dict) -> UserType:
    return UserType(
        id=strawberry.ID(str(doc["_id"])),
        username=doc["username"],
        email=doc["email"],
        role=doc["user_type"],
    )


async def list_users() -> List[UserType]:
    db = get_database()
    users = await db.users.find().to_list(length=None)
    return [_user_from_document(user) for user in users]


async def create_user(username: str, email: str, role: str) -> UserType:
    if role not in ALLOWED_USER_ROLES:
        raise ValueError(f"role must be one of {sorted(ALLOWED_USER_ROLES)}")

    db = get_database()
    user_data = {"username": username, "email": email, "user_type": role}
    result = await db.users.insert_one(user_data)
    user_data["_id"] = result.inserted_id
    return _user_from_document(user_data)


async def update_user(
    id: strawberry.ID,
    username: Optional[str] = None,
    email: Optional[str] = None,
    role: Optional[str] = None,
) -> Optional[UserType]:
    if role is not None and role not in ALLOWED_USER_ROLES:
        raise ValueError(f"role must be one of {sorted(ALLOWED_USER_ROLES)}")

    db = get_database()
    update_fields = {}
    if username is not None:
        update_fields["username"] = username
    if email is not None:
        update_fields["email"] = email
    if role is not None:
        update_fields["user_type"] = role

    if update_fields:
        await db.users.update_one({"_id": _to_object_id(id)}, {"$set": update_fields})

    updated_user = await db.users.find_one({"_id": _to_object_id(id)})
    return _user_from_document(updated_user) if updated_user else None


async def delete_user(id: strawberry.ID) -> Optional[UserType]:
    db = get_database()
    user = await db.users.find_one({"_id": _to_object_id(id)})
    if user is None:
        return None
    await db.users.delete_one({"_id": _to_object_id(id)})
    return _user_from_document(user)
