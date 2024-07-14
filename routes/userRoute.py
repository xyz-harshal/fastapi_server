from fastapi import APIRouter
from models import userRequestModel,userResponseModel
from database import db_dependancy
from schema import Peoples
from database import Base,engine
Base.metadata.create_all(bind=engine)
router=APIRouter()

@router.post("/login",response_model=userResponseModel)
async def login(req:userRequestModel,db:db_dependancy): 
    user=Peoples(email=req.email,password=req.password)
    db.add(user)
    db.commit()
    db.refresh(user)
    return {"error":False}
