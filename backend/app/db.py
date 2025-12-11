import os
import motor.motor_asyncio

DATABASE_URL = os.getenv("DATABASE_URL", "")

client = None
db = None

async def init_db():
    global client, db
    if not DATABASE_URL:
        raise RuntimeError("DATABASE_URL no está configurada")
    client = motor.motor_asyncio.AsyncIOMotorClient(DATABASE_URL)
    db_name = os.getenv("DB_NAME", None)
    db = client[db_name] if db_name else client.get_default_database()
    return db
