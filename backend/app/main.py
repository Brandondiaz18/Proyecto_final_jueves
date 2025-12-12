import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import router as todos_router
from app.db import init_db

app = FastAPI(title="Todo API - FastAPI")

# ==============================
# 🔹 CONFIGURACIÓN DE CORS
# ==============================
allowed = os.getenv("ALLOWED_ORIGIN", "*")
if allowed == "":
    allowed = "*"

origins = [o.strip() for o in allowed.split(",")] if allowed != "*" else ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ==============================
# 🔹 ENDPOINT PRINCIPAL (root)
# ==============================
@app.get("/")
def home():
    return {"message": "Backend funcionando correctamente 🚀"}

# ==============================
# 🔹 Rutas de TODOs
# ==============================
app.include_router(todos_router, prefix="/api/todos")

# ==============================
# 🔹 Evento de inicio
# ==============================
@app.on_event("startup")
async def startup_event():
    await init_db()
