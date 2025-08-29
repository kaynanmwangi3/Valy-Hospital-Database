from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models import Base

# Create SQLite database engine
engine = create_engine('sqlite:///hospital.db', echo=False)

# Create session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():
    """Initialize database tables"""
    Base.metadata.create_all(bind=engine)

def get_db():
    """Get database session"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()