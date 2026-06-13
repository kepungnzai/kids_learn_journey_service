from strawberry import Schema, type, field, mutation
from typing import List, Optional
from .types import CourseType, UserType
from .resolvers.courses import list_courses, create_course, update_course
from .resolvers.users import create_user, update_user, delete_user

@type
class Query:
    courses: List[CourseType] = field(resolver=list_courses)
    users: List[UserType] = field(resolver=list_users)

@type
class Mutation:
    create_course: CourseType = field(resolver=create_course)
    update_course: CourseType = field(resolver=update_course)
    create_user: UserType = field(resolver=create_user)
    update_user: UserType = field(resolver=update_user)
    delete_user: UserType = field(resolver=delete_user)

schema = Schema(query=Query, mutation=Mutation)