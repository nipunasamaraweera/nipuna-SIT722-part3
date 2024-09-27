from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

SQLALCHEMY_DATABASE_URL = "postgresql://nipunaazure_user:GiwrEDDjjmNqybqWtkk1j5NbYnaHvJQR@dpg-crmp781u0jms7397cn0g-a.oregon-postgres.render.com/nipunaazure" #os.getenv("DATABASE_URL")

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
