import strawberry
from typing import List, Optional
from .types import CourseType, UserType, CourseProgressType, CourseRatingType
from .resolvers.courses import list_courses, create_course, update_course
from .resolvers.users import list_users, create_user, update_user, delete_user
from .resolvers.course_progress import list_course_progress, create_course_progress, update_course_progress
from .resolvers.course_ratings import list_course_ratings, create_course_rating, update_course_rating

@strawberry.type
class Query:
    list_courses: List[CourseType] = strawberry.field(resolver=list_courses)
    users: List[UserType] = strawberry.field(resolver=list_users)
    course_progress: List[CourseProgressType] = strawberry.field(resolver=list_course_progress)
    course_ratings: List[CourseRatingType] = strawberry.field(resolver=list_course_ratings)

@strawberry.type
class Mutation:
    create_course: CourseType = strawberry.field(resolver=create_course)
    update_course: Optional[CourseType] = strawberry.field(resolver=update_course)
    create_user: UserType = strawberry.field(resolver=create_user)
    update_user: Optional[UserType] = strawberry.field(resolver=update_user)
    delete_user: Optional[UserType] = strawberry.field(resolver=delete_user)
    create_course_progress: CourseProgressType = strawberry.field(resolver=create_course_progress)
    update_course_progress: Optional[CourseProgressType] = strawberry.field(resolver=update_course_progress)
    create_course_rating: CourseRatingType = strawberry.field(resolver=create_course_rating)
    update_course_rating: Optional[CourseRatingType] = strawberry.field(resolver=update_course_rating)

schema = strawberry.Schema(query=Query, mutation=Mutation)
