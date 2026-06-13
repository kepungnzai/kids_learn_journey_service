from typing import List
import strawberry
from strawberry import auto
from ..models import Course
from ..database import get_database

@strawberry.type
class CourseType:
    id: strawberry.ID
    title: str
    description: str
    teacher_id: strawberry.ID

@strawberry.type
class Query:
    @strawberry.field
    async def courses(self) -> List[CourseType]:
        db = get_database()
        courses = await db.courses.find().to_list(length=None)
        return [CourseType(id=str(course["_id"]), title=course["title"], description=course["description"], teacher_id=course["teacher_id"]) for course in courses]

@strawberry.type
class Mutation:
    @strawberry.mutation
    async def create_course(self, title: str, description: str, teacher_id: strawberry.ID) -> CourseType:
        db = get_database()
        course = {"title": title, "description": description, "teacher_id": teacher_id}
        result = await db.courses.insert_one(course)
        return CourseType(id=str(result.inserted_id), title=title, description=description, teacher_id=teacher_id)

    @strawberry.mutation
    async def update_course(self, id: strawberry.ID, title: str, description: str) -> CourseType:
        db = get_database()
        await db.courses.update_one({"_id": id}, {"$set": {"title": title, "description": description}})
        updated_course = await db.courses.find_one({"_id": id})
        return CourseType(id=str(updated_course["_id"]), title=updated_course["title"], description=updated_course["description"], teacher_id=updated_course["teacher_id"]) 

schema = strawberry.Schema(query=Query, mutation=Mutation)