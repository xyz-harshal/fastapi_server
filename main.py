import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.authRoute import router as auth_router
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

allowed_origin = ["http://localhost:3000"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origin,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Registering multiple routers
app.include_router(auth_router, prefix="/auth")  # Auth routes

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
