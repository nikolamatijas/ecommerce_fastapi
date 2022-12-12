from fastapi import FastAPI
from ecommerce.user.router import router as user_router

app = FastAPI(title='Ecommerce App',
              version='0.0.1')

app.include_router(user_router)

