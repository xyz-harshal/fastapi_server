from fastapi import FastAPI
from routes import userRoute
from auth import jwt_encode,jwt_decode
app=FastAPI()

app.include_router(userRoute.router)
