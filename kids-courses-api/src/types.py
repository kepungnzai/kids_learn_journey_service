import strawberry
from typing import Optional

@strawberry.type
class CourseType:
    id: strawberry.ID
    title: str
    description: str
    teacher_id: Optional[strawberry.ID] = None

@strawberry.input
class CourseCreateInput:
    title: str
    description: str
    teacher_id: strawberry.ID

@strawberry.input
class CourseUpdateInput:
    title: Optional[str] = None
    description: Optional[str] = None
    teacher_id: Optional[strawberry.ID] = None

@strawberry.type
class UserType:
    id: strawberry.ID
    username: str
    email: str
    role: str

@strawberry.input
class UserCreateInput:
    username: str
    email: str
    role: str

@strawberry.input
class UserUpdateInput:
    username: Optional[str] = None
    email: Optional[str] = None
    role: Optional[str] = None


@strawberry.type
class CourseProgressType:
    id: strawberry.ID
    user_id: strawberry.ID
    course_id: strawberry.ID
    current_course_content_id: strawberry.ID


@strawberry.input
class CourseProgressCreateInput:
    user_id: strawberry.ID
    course_id: strawberry.ID
    current_course_content_id: strawberry.ID


@strawberry.input
class CourseProgressUpdateInput:
    current_course_content_id: Optional[strawberry.ID] = None


@strawberry.type
class CourseRatingType:
    id: strawberry.ID
    course_id: strawberry.ID
    author_id: strawberry.ID
    rating: int


@strawberry.input
class CourseRatingCreateInput:
    course_id: strawberry.ID
    author_id: strawberry.ID
    rating: int


@strawberry.input
class CourseRatingUpdateInput:
    rating: Optional[int] = None


@strawberry.type
class CourseContentType:
    content_id: strawberry.ID
    course_related_id: Optional[strawberry.ID] = None
    description: str
    content: str
    weblink: str
    creation_date: str
    last_update: str
    author: str
