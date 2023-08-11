from sqlalchemy import create_engine, orm
from sqlalchemy.orm import sessionmaker

from users import models
import os
from dotenv import load_dotenv
load_dotenv()

engine = create_engine(
    os.environ.get("db_url"),
    echo=True
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = orm.declarative_base()



def get_db():
    """provide db session to path operation functions"""
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

from users.models import *

# Create the tables in the database
Base.metadata.create_all(bind=engine)
