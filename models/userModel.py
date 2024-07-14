from pydantic import BaseModel

class userRequestModel(BaseModel):
    email:str
    password:str

class userResponseModel(BaseModel):
    error:bool
