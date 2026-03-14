import os
from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
DB_NAME = os.getenv("DB_NAME", "presentations_db")

if not MONGO_URI:
    raise ValueError("MONGO_URI not set in environment variables")

client = AsyncIOMotorClient(MONGO_URI)

db = client[DB_NAME]

presentations_collection = db["presentations"]