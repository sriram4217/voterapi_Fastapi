from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import settings
import time



SQLALCHEMY_DATABASE_URL = "postgresql://postgres:sriram123@localhost/fastapi"

engine = create_engine(SQLALCHEMY_DATABASE_URL)


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# while True:
#     try:
#         con=psycopg2.connect(
#         host='localhost',
#         dbname='fastapi',
#         user='postgres',
#         password="sriram123",
#         port=5432
#         )
#         cur=con.cursor()
#         break

#     except Exception as e:
#         print (e)
#         time.sleep(2)