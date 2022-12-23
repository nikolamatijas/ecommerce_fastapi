from typing import List

from fastapi import APIRouter, status, Response, HTTPException
from fastapi.params import Depends
from sqlalchemy.orm import Session

from . import services
from . import schema
from ecommerce import db
from ecommerce.auth.jwt import get_current_user
from ecommerce.user.schema import User

router = APIRouter(
    tags=['Orders'],
    prefix='/orders'
)


@router.post('/', status_code=status.HTTP_201_CREATED, response_model=schema.ShowOrder)
async def initiate_order_processing(database: Session = Depends(db.get_db),
                                    current_user: User = Depends(get_current_user)):
    result = await services.initiate_order(current_user, database)
    return result


@router.get('/', status_code=status.HTTP_200_OK, response_model=List[schema.ShowOrder])
async def orders_list(database: Session = Depends(db.get_db),
                      current_user: User = Depends(get_current_user)):
    result = await services.get_order_listing(current_user, database)
    return result
