import time
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import OperationalError
from app.core.config import settings

DATABASE_URL = (
    f"mysql+pymysql://{settings.DB_USER}:"
    f"{settings.DB_PASSWORD}@{settings.DB_HOST}/{settings.DB_NAME}"
)

MAX_RETRIES = 10
RETRY_DELAY = 3

for i in range(MAX_RETRIES):
    try:
        engine = create_engine(
            DATABASE_URL,
            pool_pre_ping=True
        )
        connection = engine.connect()
        connection.close()
        print("✅ Connected to MySQL")
        break
    except OperationalError:
        print(f"⏳ MySQL not ready... retrying ({i+1}/{MAX_RETRIES})")
        time.sleep(RETRY_DELAY)
else:
    raise Exception("❌ Could not connect to MySQL after retries")

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)