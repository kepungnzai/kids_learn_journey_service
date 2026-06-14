from typing import List, Optional
from bson import ObjectId
import strawberry
from ..database import get_database
from ..types import CourseProgressType


def _to_object_id(value: str) -> ObjectId:
    return ObjectId(str(value))


def _from_doc(doc: dict) -> CourseProgressType:
    return CourseProgressType(
        id=strawberry.ID(str(doc["_id"])),
        user_id=strawberry.ID(str(doc["user_id"])),
        course_id=strawberry.ID(str(doc["course_id"])),
        current_course_content_id=strawberry.ID(str(doc["current_course_content_id"])),
    )


async def list_course_progress(user_id: Optional[strawberry.ID] = None) -> List[CourseProgressType]:
    db = get_database()
    query = {}
    if user_id is not None:
        query["user_id"] = _to_object_id(user_id)
    docs = await db.course_progress.find(query).to_list(length=None)
    return [_from_doc(d) for d in docs]


async def create_course_progress(user_id: strawberry.ID, course_id: strawberry.ID, current_course_content_id: strawberry.ID) -> CourseProgressType:
    db = get_database()
    doc = {
        "user_id": _to_object_id(user_id),
        "course_id": _to_object_id(course_id),
        "current_course_content_id": _to_object_id(current_course_content_id),
    }
    res = await db.course_progress.insert_one(doc)
    doc["_id"] = res.inserted_id
    return _from_doc(doc)


async def update_course_progress(id: strawberry.ID, current_course_content_id: Optional[strawberry.ID] = None) -> Optional[CourseProgressType]:
    db = get_database()
    update = {}
    if current_course_content_id is not None:
        update["current_course_content_id"] = _to_object_id(current_course_content_id)
    if update:
        await db.course_progress.update_one({"_id": _to_object_id(id)}, {"$set": update})
    doc = await db.course_progress.find_one({"_id": _to_object_id(id)})
    return _from_doc(doc) if doc else None
