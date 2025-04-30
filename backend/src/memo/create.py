from fastapi import APIRouter, HTTPException
from ..models.memo import MemoCreateModel, MemoModel
from ..prisma_client import prisma

router = APIRouter()

@router.post("/memoData", response_model=MemoModel)
async def create_memo(memo: MemoCreateModel):
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