from sqlalchemy import String,Integer,Column,Boolean,ForeignKey
from database import Base

class Peoples(Base):
    __tablename__="peoples"

    id=Column(Integer,primary_key=True,index=True)
    email=Column(String,index=True)
    password=Column(String,index=True)

