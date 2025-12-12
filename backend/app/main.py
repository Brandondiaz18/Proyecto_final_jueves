import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import router as todos_router
from app.db import init_db

app = FastAPI(title="Todo API - FastAPI")

# ================================
# 🔥 CORS CONFIG CORRECTA
# ================================
origins = [
    "http://localhost:5173",                         # Frontend local
    "https://proyecto-final-frontend.onrender.com",  # Tu frontend en Render
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ================================
# 🔥 ENDPOINT RAÍZ (obligatorio para evitar 404 en Render)
# ================================
@app.get("/")
def root():
    return {"message": "Backend funcionando correctamente 🚀"}


# ================================
# 🔥 RUTAS PRINCIPALES
# ================================
app.include_router(todos_router, prefix="/api/todos")


# ================================
# 🔥 INICIALIZAR BASE DE DATOS
# ================================
@app.on_event("startup")
async def startup_event():
    await init_db()
