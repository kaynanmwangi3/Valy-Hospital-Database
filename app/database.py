from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models import Base

# Create SQLite database engine
engine = create_engine('sqlite:///hospital.db', echo=False)

# Create session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# create database tables
def init_db():
    Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()