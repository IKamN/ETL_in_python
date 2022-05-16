# Import the module required
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine(
    "postgresql+psycopg2://postgres:7627@localhost:5432/datacamp"
)

# Initialize the session
session = Session(engine)

# Initialize the declarative base
Base = declarative_base()
