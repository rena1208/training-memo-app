from contextlib import asynccontextmanager
from fastapi import FastAPI
from .prisma_client import prisma
from .memo import list, create, update

@asynccontextmanager
async def lifespan(app: FastAPI):
    await prisma.connect()
    yield
    await prisma.disconnect()

app = FastAPI(lifespan=lifespan)

app.include_router(list.router, prefix="/api")
app.include_router(create.router, prefix="/api")
app.include_router(update.router, prefix="/api")

@app.get("/api")
async def root():
    return {"message": "Hello World"}