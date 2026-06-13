from typing import List, Optional
from bson import ObjectId
import strawberry
from ..database import get_database
from ..types import CourseType


def _to_object_id(value: str) -> ObjectId:
    return ObjectId(str(value))


def _course_from_document(doc: dict) -> CourseType:
    return CourseType(
        id=strawberry.ID(str(doc["_id"])),
        title=doc["title"],
        description=doc.get("description", ""),
        teacher_id=strawberry.ID(str(doc["teacher_id"])) if doc.get("teacher_id") else None,
    )


async def list_courses() -> List[CourseType]:
    db = get_database()
    courses = await db.courses.find().to_list(length=None)
    return [_course_from_document(course) for course in courses]


async def create_course(title: str, description: str, teacher_id: strawberry.ID) -> CourseType:
    db = get_database()
    course_data = {
        "title": title,
        "description": description,
        "teacher_id": _to_object_id(teacher_id),
    }
    result = await db.courses.insert_one(course_data)
    course_data["_id"] = result.inserted_id
    return _course_from_document(course_data)


async def update_course(
    id: strawberry.ID,
    title: Optional[str] = None,
    description: Optional[str] = None,
    teacher_id: Optional[strawberry.ID] = None,
) -> Optional[CourseType]:
    db = get_database()
    update_fields = {}
    if title is not None:
        update_fields["title"] = title
    if description is not None:
        update_fields["description"] = description
    if teacher_id is not None:
        update_fields["teacher_id"] = _to_object_id(teacher_id)

    if update_fields:
        await db.courses.update_one({"_id": _to_object_id(id)}, {"$set": update_fields})

    updated_course = await db.courses.find_one({"_id": _to_object_id(id)})
    return _course_from_document(updated_course) if updated_course else None
