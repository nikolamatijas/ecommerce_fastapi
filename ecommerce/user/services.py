from typing import Optional

from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from . import schema
from .models import User


async def new_user_register(request: schema.User, database: Session) -> User:
    new_user = User(name=request.name, email=request.email, password=request.password)
    database.add(new_user)
    database.commit()
    database.refresh(new_user)
    return new_user


async def all_users(database: Session):
    return database.query(User).all()


async def get_user_by_id(user_id: int, database: Session) -> Optional[User]:
    user_info = database.query(User).get(user_id)
    if not user_info:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User not found.')
    return user_info


async def delete_user_by_id(user_id: int, database: Session):
    database.query(User).filter(User.id == user_id).delete()
    database.commit()
