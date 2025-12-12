from fastapi import APIRouter, HTTPException
from app.db import get_db
from app.models import TodoIn, TodoUpdate
from datetime import datetime
from bson import ObjectId

router = APIRouter()  # NO AGREGAR prefijos aquí


def get_collection():
    return get_db()["todos"]


# ---------------- LISTAR ----------------
@router.get("/")
async def list_todos():
    coll = get_collection()
    cursor = coll.find().sort("created_at", -1)

    docs = []
    async for doc in cursor:
        docs.append({
            "id": str(doc["_id"]),
            "title": doc.get("title"),
            "description": doc.get("description"),
            "status": doc.get("status", "pendiente"),
            "created_at": doc.get("created_at")
        })
    return docs


# ---------------- CREAR ----------------
@router.post("/")
async def create_todo(payload: TodoIn):
    coll = get_collection()

    if not payload.title or payload.title.strip() == "":
        raise HTTPException(400, "El título es obligatorio")

    now = datetime.utcnow()

    doc = {
        "title": payload.title.strip(),
        "description": payload.description,
        "status": "pendiente",
        "created_at": now
    }

    res = await coll.insert_one(doc)
    doc["id"] = str(res.inserted_id)

    return doc


# ---------------- ACTUALIZAR ----------------
@router.put("/{id}")
async def update_todo(id: str, payload: TodoUpdate):
    coll = get_collection()

    if not ObjectId.is_valid(id):
        raise HTTPException(400, "ID inválido")

    update = {}

    if payload.title is not None:
        update["title"] = payload.title
    if payload.description is not None:
        update["description"] = payload.description
    if payload.status is not None:
        if payload.status not in ("pendiente", "completada"):
            raise HTTPException(400, "Status inválido")
        update["status"] = payload.status

    if update == {}:
        raise HTTPException(400, "Nada para actualizar")

    res = await coll.find_one_and_update(
        {"_id": ObjectId(id)},
        {"$set": update},
        return_document=True
    )

    if not res:
        raise HTTPException(404, "Tarea no encontrada")

    return {
        "id": str(res["_id"]),
        "title": res.get("title"),
        "description": res.get("description"),
        "status": res.get("status"),
        "created_at": res.get("created_at")
    }


# ---------------- BORRAR ----------------
@router.delete("/{id}")
async def delete_todo(id: str):
    coll = get_collection()

    if not ObjectId.is_valid(id):
        raise HTTPException(400, "ID inválido")

    res = await coll.delete_one({"_id": ObjectId(id)})

    if res.deleted_count == 0:
        raise HTTPException(404, "Tarea no encontrada")

    return {"message": "Eliminada correctamente"}
