from datetime import datetime
from typing import List, Optional

import strawberry
from bson import ObjectId

from ..database import get_database
from ..types import CourseContentType


def _to_object_id(value: str) -> ObjectId:
    return ObjectId(str(value))


def _course_content_from_document(doc: dict) -> CourseContentType:
    creation_date = doc.get("creation_date")
    last_update = doc.get("last_update")

    return CourseContentType(
        content_id=strawberry.ID(str(doc["_id"])),
        course_related_id=strawberry.ID(str(doc["course_related_id"])) if doc.get("course_related_id") else None,
        description=doc.get("description", ""),
        content=doc.get("content", ""),
        weblink=doc.get("weblink", ""),
        creation_date=creation_date.isoformat() if isinstance(creation_date, datetime) else str(creation_date or ""),
        last_update=last_update.isoformat() if isinstance(last_update, datetime) else str(last_update or ""),
        author=doc.get("author", ""),
    )


async def list_course_contents() -> List[CourseContentType]:
    db = get_database()
    contents = await db.course_content.find().to_list(length=None)
    return [_course_content_from_document(content) for content in contents]


async def create_course_content(
    course_related_id: strawberry.ID,
    description: str,
    content: str,
    weblink: Optional[str] = None,
    author: Optional[str] = None,
) -> CourseContentType:
    db = get_database()
    now = datetime.utcnow()
    content_data = {
        "course_related_id": _to_object_id(course_related_id),
        "description": description,
        "content": content,
        "weblink": weblink or "",
        "creation_date": now,
        "last_update": now,
        "author": author or "",
    }
    result = await db.course_content.insert_one(content_data)
    content_data["_id"] = result.inserted_id
    return _course_content_from_document(content_data)


async def update_course_content(
    content_id: strawberry.ID,
    description: Optional[str] = None,
    content: Optional[str] = None,
    weblink: Optional[str] = None,
    author: Optional[str] = None,
) -> Optional[CourseContentType]:
    db = get_database()
    update_fields = {}
    if description is not None:
        update_fields["description"] = description
    if content is not None:
        update_fields["content"] = content
    if weblink is not None:
        update_fields["weblink"] = weblink
    if author is not None:
        update_fields["author"] = author

    if update_fields:
        update_fields["last_update"] = datetime.utcnow()
        await db.course_content.update_one({"_id": _to_object_id(content_id)}, {"$set": update_fields})

    updated_content = await db.course_content.find_one({"_id": _to_object_id(content_id)})
    return _course_content_from_document(updated_content) if updated_content else None
