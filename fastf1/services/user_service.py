from sqlalchemy.orm import Session
from fastf1.repositories.user_repository import UserRepository

class UserService:

    @staticmethod
    def list_users(db: Session):
        return UserRepository.get_all(db)

    @staticmethod
    def create_user(db: Session, user_data):
        return UserRepository.create(db, user_data)

    @staticmethod
    def get_user(db: Session, user_id: int):
        user = UserRepository.get_by_id(db, user_id)
        if not user:
            raise ValueError("User not found")
        return user
