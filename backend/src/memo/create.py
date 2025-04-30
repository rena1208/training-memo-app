from fastapi import APIRouter, HTTPException
from ..models.memo import MemoCreateModel, MemoModel
from ..prisma_client import prisma

router = APIRouter()

@router.post("/memoData", response_model=MemoModel)
async def create_memo(memo: MemoCreateModel):
    try:
        print(f"受信タイトル: {memo.title}, 本文: {memo.content}")
        created = await prisma.memo.create(
            data={
                "title": memo.title,
                "content": memo.content,
            }
        )
        return created
    except Exception as e:
        print(f"エラー発生: {e}")
        raise HTTPException(status_code=500, detail="Memo作成に失敗しました")