import strawberry
from typing import List, Optional
from .types import CourseType, UserType
from .resolvers.courses import list_courses, create_course, update_course
from .resolvers.users import list_users, create_user, update_user, delete_user

@strawberry.type
class Query:
    list_courses: List[CourseType] = strawberry.field(resolver=list_courses)
    users: List[UserType] = strawberry.field(resolver=list_users)

@strawberry.type
class Mutation:
    create_course: CourseType = strawberry.field(resolver=create_course)
    update_course: Optional[CourseType] = strawberry.field(resolver=update_course)
    create_user: UserType = strawberry.field(resolver=create_user)
    update_user: Optional[UserType] = strawberry.field(resolver=update_user)
    delete_user: Optional[UserType] = strawberry.field(resolver=delete_user)

schema = strawberry.Schema(query=Query, mutation=Mutation)
