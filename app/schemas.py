from pydantic import BaseModel
from typing import Optional


class CounterCreate(BaseModel):
    name: str
    value: int = 0


class CounterUpdate(BaseModel):
    value: Optional[int] = None


class CounterResponse(BaseModel):
    id: int
    name: str
    value: int
    created_at: str
    updated_at: str