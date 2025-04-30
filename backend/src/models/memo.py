from pydantic import BaseModel
from datetime import datetime

# レスポンス用のモデル
class MemoModel(BaseModel):
    id: int
    title: str
    content: str
    createdAt: datetime
    updatedAt: datetime

# リクエスト（post）用のモデル
class MemoCreateModel(BaseModel):
    title: str
    content: str