from datetime import datetime

from sqlalchemy import Column, String, Float, ForeignKey, Text, DateTime, Integer
from sqlalchemy.orm import relationship

from ecommerce.db import Base
from ecommerce.products.models import Product
from ecommerce.user.models import User


class Order(Base):
    __tablename__ = 'order'

    id = Column(Integer, primary_key=True, autoincrement=True)
    order_date = Column(DateTime, default=datetime.now)
    order_amount = Column(Float, default=0.0)
    order_status = Column(String, default='PROCESSING')
    shipping_address = Column(Text)
    customer_id = Column(Integer, ForeignKey(User.id, ondelete='CASCADE'))

    order_details = relationship('OrderDetails', back_populates='order')
    user_info = relationship('User', back_populates='order')


class OrderDetails(Base):
    __tablename__ = 'order_details'

    id = Column(Integer, primary_key=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey('order.id', ondelete='CASCADE'))
    product_id = Column(Integer, ForeignKey(Product.id, ondelete='CASCADE'))
    quantity = Column(Integer, default=1)
    created = Column(DateTime, default=datetime.now)

    order = relationship('Order', back_populates='order_details')
    product_order_details = relationship('Product', back_populates='order_details')
