from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,DeclarativeBase

SQLALCHEMY_DATABASE_URL = "postgresql://postgres:admin%40123@localhost/todoapp"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


class Base(DeclarativeBase):
    pass
