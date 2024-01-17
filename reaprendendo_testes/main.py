from fastapi import FastAPI

fastapi = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()