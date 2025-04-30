from fastapi import FastAPI

app = FastAPI()

# @app.get("/")
@app.get("/api")
async def root():
    return {"message": "Hello World"}