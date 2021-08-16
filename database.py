from sqlalchemy import create_engine

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import sessionmaker


MYSQL_DATABASE_URL = "mysql+pymysql://" + "root:aspire" + "@localhost/eduvirintsa?charset=utf8mb4"

engine = create_engine(
    MYSQL_DATABASE_URL, connect_args={}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


