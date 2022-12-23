from fastapi import HTTPException, status
from fastapi.params import Depends
from sqlalchemy.orm import Session

from ecommerce import db
from ecommerce.cart.models import Cart, CartItems
from ecommerce.products.models import Product
from ecommerce.user import schema
from ecommerce.user.models import User


async def add_items(cart_id: int, product_id: int, database: Session = Depends(db.get_db)):
    cart_items = CartItems(cart_id=cart_id, product_id=product_id)
    database.add(cart_items)
    database.commit()
    database.refresh(cart_items)


async def add_to_cart(product_id, current_user, database: Session = Depends(db.get_db)):
    product_info = database.query(Product).get(product_id)
    if not product_info:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Product not found.')

    if product_info.quantity <= 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Product out of stock.')

    user_info = database.query(User).filter(User.email == current_user.email).first()
    cart_info = database.query(Cart).filter(Cart.user_id == user_info.id).first()
    if not cart_info:
        cart_info = Cart(user_id=user_info.id)
        database.add(cart_info)
        database.commit()
        database.refresh(cart_info)

    await add_items(cart_info.id, product_info.id, database)
    return {'status': 'Item added to cart.'}


async def get_all_cart_items(current_user, database: Session = Depends(db.get_db)):
    user_info = database.query(User).filter(User.email == current_user.email).first()
    cart = database.query(Cart).filter(Cart.user_id == user_info.id).first()
    return cart


async def remove_item_from_cart(cart_item_id, current_user, database: Session) -> None:
    user_info = database.query(User).filter(User.email == current_user.email).first()
    cart = database.query(Cart).filter(Cart.user_id == user_info.id).first()
    database.query(CartItems).filter(CartItems.id == cart_item_id,
                                     CartItems.cart_id == cart.id).delete()
    database.commit()
    return
