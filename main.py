from fastapi import FastAPI
import uvicorn
from logging_config import logger


app = FastAPI()


@app.get("/")
def index():
    logger.info("Index API triggered")
    return {"message": "Docker volumes"}

if __name__ == "__main__":
    # uvicorn.run(app=app, host="127.0.0.1", port=8080)
    uvicorn.run(app=app, host="0.0.0.0", port=8080)
