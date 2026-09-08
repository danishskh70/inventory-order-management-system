from sqlalchemy.orm import sessionmaker

from app.core.config import settings
from sqlalchemy import create_engine


engine=create_engine(settings.database_url)
SessionLocal=sessionmaker(autocommit=False,autoflush=False,bind=engine)

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()

        