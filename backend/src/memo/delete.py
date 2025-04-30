from fastapi import APIRouter, HTTPException
from ..models.memo import MemoResponse
from ..prisma_client import prisma

router = APIRouter()

@router.delete("memo/{id}", response_model=MemoResponse)
async def delete_todo(id: int):
    existing = await prisma.todo.find_unique(where={"id": id})
    if not existing:
        raise HTTPException(status_code=404, detail="todoが見つかりません")

    deleted = await prisma.todo.delete(
        where={"id": id}
    )
    return deleted