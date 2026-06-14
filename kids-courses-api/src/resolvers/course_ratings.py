from typing import List, Optional
from bson import ObjectId
import strawberry
from ..database import get_database
from ..types import CourseRatingType


def _to_object_id(value: str) -> ObjectId:
    return ObjectId(str(value))


def _from_doc(doc: dict) -> CourseRatingType:
    return CourseRatingType(
        id=strawberry.ID(str(doc["_id"])),
        course_id=strawberry.ID(str(doc["course_id"])),
        author_id=strawberry.ID(str(doc["author_id"])),
        rating=int(doc.get("rating", 0)),
    )


async def list_course_ratings(course_id: Optional[strawberry.ID] = None) -> List[CourseRatingType]:
    db = get_database()
    query = {}
    if course_id is not None:
        query["course_id"] = _to_object_id(course_id)
    docs = await db.course_ratings.find(query).to_list(length=None)
    return [_from_doc(d) for d in docs]


async def create_course_rating(course_id: strawberry.ID, author_id: strawberry.ID, rating: int) -> CourseRatingType:
    if rating < 0:
        raise ValueError("rating must be a non-negative integer")
    db = get_database()
    doc = {
        "course_id": _to_object_id(course_id),
        "author_id": _to_object_id(author_id),
        "rating": int(rating),
    }
    res = await db.course_ratings.insert_one(doc)
    doc["_id"] = res.inserted_id
    return _from_doc(doc)


async def update_course_rating(id: strawberry.ID, rating: Optional[int] = None) -> Optional[CourseRatingType]:
    if rating is not None and rating < 0:
        raise ValueError("rating must be a non-negative integer")
    db = get_database()
    update = {}
    if rating is not None:
        update["rating"] = int(rating)
    if update:
        await db.course_ratings.update_one({"_id": _to_object_id(id)}, {"$set": update})
    doc = await db.course_ratings.find_one({"_id": _to_object_id(id)})
    return _from_doc(doc) if doc else None
