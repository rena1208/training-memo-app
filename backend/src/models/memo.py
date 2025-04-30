from pydantic import BaseModel
from datetime import datetime

class MemoModel(BaseModel):
    id: int
    title: str
    content: str
    createdAt: datetime
    updatedAt: datetime