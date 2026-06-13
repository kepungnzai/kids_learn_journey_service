from typing import List, Optional
import strawberry
from strawberry import auto
from ..models import User
from ..database import get_user_collection

@strawberry.type
class UserType:
    id: str
    username: str
    email: str
    user_type: str  # 'student', 'teacher', or 'admin'

@strawberry.type
class Query:
    users: List[UserType] = strawberry.field(resolver=lambda: list(get_user_collection().find()))
    
    @strawberry.field
    def user(self, id: str) -> Optional[UserType]:
        user_data = get_user_collection().find_one({"_id": id})
        return UserType(**user_data) if user_data else None

@strawberry.type
class Mutation:
    @strawberry.mutation
    def create_user(self, username: str, email: str, user_type: str) -> UserType:
        user_data = {"username": username, "email": email, "user_type": user_type}
        result = get_user_collection().insert_one(user_data)
        user_data["_id"] = str(result.inserted_id)
        return UserType(**user_data)

    @strawberry.mutation
    def update_user(self, id: str, username: Optional[str] = None, email: Optional[str] = None, user_type: Optional[str] = None) -> Optional[UserType]:
        update_data = {k: v for k, v in {"username": username, "email": email, "user_type": user_type}.items() if v is not None}
        if update_data:
            get_user_collection().update_one({"_id": id}, {"$set": update_data})
        user_data = get_user_collection().find_one({"_id": id})
        return UserType(**user_data) if user_data else None

    @strawberry.mutation
    def delete_user(self, id: str) -> bool:
        result = get_user_collection().delete_one({"_id": id})
        return result.deleted_count > 0

schema = strawberry.Schema(query=Query, mutation=Mutation)