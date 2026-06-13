from strawberry import type, ID

@type
class Course:
    id: ID
    title: str
    description: str
    teacher_id: ID

@type
class User:
    id: ID
    username: str
    email: str
    user_type: str  # Can be 'student', 'teacher', or 'admin'