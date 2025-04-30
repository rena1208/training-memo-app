from fastapi import APIRouter, HTTPException
from ..models.memo import MemoRequest, MemoResponse
from ..prisma_client import prisma

router = APIRouter()

@router.post("/memo-data", response_model=MemoResponse)
async def create_memo(memo: MemoRequest):
    try:
        created = await prisma.memo.create(
            data={
                "title": memo.title,
                "content": memo.content,
            }
        )
        return created
    except Exception:
        raise HTTPException(status_code=500, detail="Memo作成に失敗しました")