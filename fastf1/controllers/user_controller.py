from sqlalchemy.orm import Session
from fastf1.services.user_service import UserService

class UserController:

    @staticmethod
    def list_users(db: Session):
        return UserService.list_users(db)

    @staticmethod
    def create_user(db: Session, data):
        return UserService.create_user(db, data)

    @staticmethod
    def get_user(db: Session, user_id: int):
        return UserService.get_user(db, user_id)
