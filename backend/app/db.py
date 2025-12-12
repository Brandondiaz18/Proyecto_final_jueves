import os
import motor.motor_asyncio

client = None
db = None

async def init_db():
    global client, db

    DATABASE_URL = os.getenv("DATABASE_URL")
    DB_NAME = os.getenv("DB_NAME")

    if not DATABASE_URL:
        raise RuntimeError("DATABASE_URL no está configurada")

    if not DB_NAME:
        raise RuntimeError("DB_NAME no está configurada")

    client = motor.motor_asyncio.AsyncIOMotorClient(DATABASE_URL)
    db = client[DB_NAME]

    print("MongoDB conectado correctamente")

    return db
