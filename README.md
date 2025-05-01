# training-memo-app

##  フロントエンドサーバー起動
```
cd frontend
pnpm run dev
```

## バックエンドサーバー起動
```
cd backend
docker compose up -d
source .venv/bin/activate
uvicorn src.main:app --reload
```
