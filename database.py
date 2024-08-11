from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,Session
from fastapi import Depends
from sqlalchemy.ext.declarative import declarative_base
from typing import Annotated
import models

url_database='postgresql://postgres.tiqriynlomatzjzpqkbf:LZRmYtcQOg77uMUY@aws-0-ap-south-1.pooler.supabase.com:6543/postgres'
engine=create_engine(url_database)
sessionlocal=sessionmaker(autocommit=False,autoflush=False,bind=engine)

Base=declarative_base()

def db_connect():
    db=sessionlocal()
    try:
        yield db
    finally:
        db.close()

db_dependancy=Annotated[Session,Depends(db_connect)]
