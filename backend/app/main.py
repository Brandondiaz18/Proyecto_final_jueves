import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import router as todos_router
from app.db import init_db

app = FastAPI(title="Todo API - FastAPI")

# 🔥 CORS 100% ABIERTO (solo para pruebas)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],          # PERMITIR TODO
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 🔥 Endpoint raíz (para evitar 404 y que CORS falle)
@app.get("/")
async def root():
    return {"message": "Backend funcionando correctamente 🚀"}

# 🔥 Tus rutas reales
app.include_router(todos_router, prefix="/api/todos")

# 🔥 Inicializar DB
@app.on_event("startup")
async def startup_event():
    await init_db()
