from fastapi import APIRouter, HTTPException
from app.db import get_db
from app.models import TodoIn, TodoUpdate
from datetime import datetime
from bson import ObjectId

router = APIRouter()


# Convertir documentos de Mongo a JSON seguro
def serialize_todo(doc):
    return {
        "id": str(doc["_id"]),
        "title": doc.get("title", ""),
        "description": doc.get("description", ""),
        "status": doc.get("status", "pendiente"),
        "created_at": str(doc.get("created_at"))
    }


def get_collection():
    return get_db()["todos"]


# ---------------- LISTAR ----------------
@router.get("/", status_code=200)
async def list_todos():
    coll = get_collection()
    cursor = coll.find().sort("created_at", -1)

    todos = []
    async for doc in cursor:
        todos.append(serialize_todo(doc))

    return todos


# ---------------- CREAR ----------------
@router.post("/", status_code=201)
async def create_todo(payload: TodoIn):
    coll = get_collection()

    if not payload.title or payload.title.strip() == "":
        raise HTTPException(status_code=400, detail="El título es obligatorio")

    now = datetime.utcnow()

    doc = {
        "title": payload.title.strip(),
        "description": payload.description,
        "status": "pendiente",
        "created_at": now
    }

    res = await coll.insert_one(doc)
    new_doc = await coll.find_one({"_id": res.inserted_id})

    return serialize_todo(new_doc)


# ---------------- ACTUALIZAR ----------------
@router.put("/{id}", status_code=200)
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

    await coll.update_one(
        {"_id": ObjectId(id)},
        {"$set": update}
    )

    updated = await coll.find_one({"_id": ObjectId(id)})

    if not updated:
        raise HTTPException(404, "Tarea no encontrada")

    return serialize_todo(updated)


# ---------------- BORRAR ----------------
@router.delete("/{id}", status_code=200)
async def delete_todo(id: str):
    coll = get_collection()

    if not ObjectId.is_valid(id):
        raise HTTPException(400, "ID inválido")

    result = await coll.delete_one({"_id": ObjectId(id)})

    if result.deleted_count == 0:
        raise HTTPException(404, "Tarea no encontrada")

    return {"message": "Eliminada correctamente"}
