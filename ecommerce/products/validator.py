from typing import Optional

from sqlalchemy.orm import Session

from .models import Category


async def verifiy_category_exists(category_id, db_session: Session) -> Optional[Category]:
    return db_session.query(Category).filter(Category.id == category_id).first()
