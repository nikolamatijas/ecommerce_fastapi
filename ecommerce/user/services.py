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
