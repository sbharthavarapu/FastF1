from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from fastf1.dependencies import get_db
from fastf1.controllers.user_controller import UserController
from fastf1.schemas.user_schema import UserCreate, UserResponse

router = APIRouter(prefix="/users", tags=["Users"])

@router.get("/", response_model=list[UserResponse])
def list_users(db: Session = Depends(get_db)):
    return UserController.list_users(db)

@router.post("/", response_model=UserResponse)
def create_user(data: UserCreate, db: Session = Depends(get_db)):
    return UserController.create_user(db, data.model_dump())

@router.get("/{user_id}", response_model=UserResponse)
def get_user(user_id: int, db: Session = Depends(get_db)):
    return UserController.get_user(db, user_id)
