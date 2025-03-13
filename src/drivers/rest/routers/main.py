from fastapi import FastAPI

from src.configs.database_config import connection

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)