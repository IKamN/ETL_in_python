# Import the module required
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, declarative_base

engine = create_engine(
    "postgresql+psycopg2://repl:S3cretPassw0rd@localhost:5432/campdata_prod"
)

# Initialize the session
session = Session(engine)

# Initialize the declarative base
Base = declarative_base()