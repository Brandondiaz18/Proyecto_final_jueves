import os
import motor.motor_asyncio

DATABASE_URL = os.getenv("DATABASE_URL")
DB_NAME = os.getenv("DB_NAME")

client = None
db = None

async def init_db():
    global client, db

    if not DATABASE_URL:
        raise RuntimeError("DATABASE_URL no está configurada")

    client = motor.motor_asyncio.AsyncIOMotorClient(DATABASE_URL)

    if not DB_NAME:
        raise RuntimeError("DB_NAME no está configurada")

    db = client[DB_NAME]  # guardar la base correctamente

    print("📌 Base de datos inicializada correctamente")

    return db

def get_db():
    if db is None:
        raise RuntimeError("DB no inicializada")
    return db
