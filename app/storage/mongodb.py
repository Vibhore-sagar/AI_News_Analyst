from motor.motor_asyncio import AsyncIOMotorClient
from app.core.settings import settings
import logging

logger = logging.getLogger("ainews.mongodb")

class MongoDB:
    client: AsyncIOMotorClient = None
    db = None

db_client = MongoDB()

async def connect_to_mongo():
    logger.info("Connecting to MongoDB...")
    db_client.client = AsyncIOMotorClient(settings.MONGODB_URL)
    db_client.db = db_client.client[settings.MONGO_DB_NAME]
    logger.info("Connected to MongoDB!")

async def close_mongo_connection():
    if db_client.client:
        db_client.client.close()
        logger.info("MongoDB connection closed.")

def get_db():
    return db_client.db
