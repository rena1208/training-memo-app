from fastapi import APIRouter, HTTPException
from ..models.memo import MemoResponse, MemoRequest
from ..prisma_client import prisma

router = APIRouter()

@router.patch("/memo-data/{id}", response_model=MemoResponse)
async def update_memo(id: int, memo: MemoRequest):
    try:
        existing = await prisma.memo.find_unique(where={"id": id})
        if not existing:
            raise HTTPException(status_code=404, detail="memoが見つかりません")

        updated = await prisma.memo.update(
            where={"id": id},
            data={
                "title": memo.title,
                "content": memo.content,
            }
        )
        return updated
    
    except Exception:
        raise HTTPException(status_code=500, detail="Memoの更新に失敗しました")
