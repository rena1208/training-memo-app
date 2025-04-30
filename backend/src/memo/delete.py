from fastapi import APIRouter, HTTPException
from ..models.memo import MemoResponse
from ..prisma_client import prisma

router = APIRouter()

@router.delete("memo/{id}", response_model=MemoResponse)
async def delete_todo(id: int):
    try:
        existing = await prisma.memo.find_unique(where={"id": id})
        if not existing:
            raise HTTPException(status_code=404, detail="memoが見つかりません")

        deleted = await prisma.memo.delete(
            where={"id": id}
        )
        return deleted
    
    except Exception:
        raise HTTPException(status_code=500, detail="Memoの削除に失敗しました")