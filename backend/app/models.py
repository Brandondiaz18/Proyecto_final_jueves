from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class TodoIn(BaseModel):
    title: str = Field(..., min_length=1)
    description: Optional[str] = None

class TodoUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    status: Optional[str] = None  # "pendiente" | "completada"
