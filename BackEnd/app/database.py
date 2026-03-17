from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

SERVER = "(localdb)\\TestTB"
DATABASE = "DBDAPI"

DATABASE_URL = (
    f"mssql+pyodbc://@{SERVER}/{DATABASE}"
    "?driver=ODBC+Driver+17+for+SQL+Server"
    "&trusted_connection=yes"
)

engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True   # ป้องกัน connection หลุด
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        return db
    except:
        db.close()
        raise