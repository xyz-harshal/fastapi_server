# FastAPI Server Code Generation Guidelines

This document provides strict instructions for LLM models to generate code for the FastAPI server project. Follow these guidelines precisely to maintain consistency and proper project structure.

## Project Structure

Maintain the following directory structure strictly:
```
- auth.py
- copilot-instructions.md
- database.py
- main.py
- readme.md
- requirement.txt
- __pycache__/
- models/
    - __init__.py
    - <new_model_file>.py
- routes/
    - __init__.py
    - <new_route_file>.py
```

### File Descriptions

1. **main.py**
   - This file will import all the routes from the `routes` directory.
   - Ensure all routes are properly registered with the FastAPI app instance.

2. **database.py**
   - This file will remain unchanged and handle database connections and configurations.

3. **auth.py**
   - This file will remain unchanged and handle authentication logic.

4. **models/**
   - Each new set of routes must have a corresponding model file in this directory.
   - The model files should be concise, modular, and follow best practices.

5. **routes/**
   - Maintain a modular structure for all routes.
   - Each route file must follow the code template of `routes/userRoute.py`.
   - Ensure proper error handling and simplicity in the generated code.

## Code Generation Norms

- **Simplicity**: The generated code must be concise and workable.
- **Error Handling**: Include proper error handling mechanisms.
- **Best Practices**: Follow industry best practices for FastAPI development.
- **No Excess Code**: Avoid generating unnecessary or redundant code.
- **Documentation**: Add clear and concise docstrings for all functions and classes.
- **Type Annotations**: Use type annotations for all function arguments and return types.
- **Environment Variables**: Validate and handle missing environment variables gracefully.
- **Security**: Ensure secure handling of sensitive data, such as passwords and API keys.
- **Testing**: Include unit tests for critical functions and routes.

## Route Code Template

All generated route files must adhere to the following template:

```python
from fastapi import APIRouter, HTTPException

router = APIRouter()

@router.get("/example")
def example_route():
    """Example route to demonstrate the template."""
    try:
        # Your logic here
        return {"message": "Example route"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
```

## Example: `routes/userRoute.py`

Below is an example of a route file (`routes/userRoute.py`) that must be followed for all new route files:

```python
from fastapi import APIRouter, HTTPException
from supabase import create_client, Client
import os
import uuid
from auth import hashed_pass, verify_hash_pass
from models import userReqMod, userResMod

router = APIRouter()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

if not SUPABASE_URL or not SUPABASE_KEY:
    raise ValueError("SUPABASE_URL and SUPABASE_KEY environment variables must be set")

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

@router.post("/login", response_model=userResMod)
async def login(req: userReqMod):
    """Login route to authenticate users."""
    try:
        response = supabase.table("users").select("uid, password, username").eq("email", req.email).single().execute()
        if not response.data:
            return {"error": True, "token": "", "username": ""}
        user = response.data
        if not verify_hash_pass(req.password, user["password"]):
            return {"error": True, "token": "", "username": ""}
        return {"error": False, "token": user["uid"], "username": user["username"]}
    except Exception as e:
        print(f"Login error: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")

@router.post("/register", response_model=userResMod)
async def register(req: userReqMod):
    """Register route to create new users."""
    try:
        if not req.username:
            return {"error": True, "token": "", "username": ""}
        response = supabase.table("users").select("uid").eq("email", req.email).execute()
        if response.data:
            return {"error": True, "token": "", "username": ""}
        hash_pass = hashed_pass(req.password)
        response = supabase.table("users").insert({
            "uid": str(uuid.uuid4()),
            "email": req.email,
            "password": hash_pass,
            "username": req.username
        }).execute()
        user_id = response.data[0]["uid"]
        return {"error": False, "token": user_id, "username": req.username}
    except Exception as e:
        print(f"Registration error: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")
```

## cURL Command Generation

For every route generated, provide a corresponding cURL command to test the route. For example:

```bash
curl -X GET "http://127.0.0.1:8000/example" -H "accept: application/json"
```

## Final Note

Adhere to these guidelines strictly to ensure consistency, maintainability, and quality of the FastAPI server project.
