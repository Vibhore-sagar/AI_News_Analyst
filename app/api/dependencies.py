from fastapi import Request
from app.storage.mongodb import get_db

async def get_database():
    db = get_db()
    if db is None:
        raise Exception("Database not initialized")
    return db
