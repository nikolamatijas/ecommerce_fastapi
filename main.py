from fastapi import FastAPI
from ecommerce.user.router import router as user_router
from ecommerce.products.router import router as product_router
from ecommerce.cart.router import router as cart_router
from ecommerce.orders.router import router as orders_router

app = FastAPI(title='Ecommerce App',
              version='0.0.1')

app.include_router(user_router)
app.include_router(product_router)
app.include_router(cart_router)
app.include_router(orders_router)


