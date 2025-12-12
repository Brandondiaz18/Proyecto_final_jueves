from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import router as todos_router
from app.db import init_db

app = FastAPI(title="Todo API - FastAPI")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # permitir TODO (temporalmente)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "Backend funcionando correctamente 🚀"}

# Importante: este endpoint debe ser EXACTAMENTE así:
app.include_router(todos_router, prefix="/api/todos")

@app.on_event("startup")
async def startup_event():
    await init_db()
