from fastapi import APIRouter, HTTPException
from ..models.memo import MemoResponse
from ..main import prisma
from prisma import errors as prisma_errors

router = APIRouter()

@router.get("/memo-data")
async def get_memo_lists(page: int = 1) -> list[MemoResponse]:
    per_page = 6
    try:
        return await prisma.memo.find_many(
            take=per_page,
            skip=(page - 1) * per_page
        )
    except prisma_errors.PrismaError as e:
        print(e)
        raise HTTPException(status_code=400, detail="fetch failed")