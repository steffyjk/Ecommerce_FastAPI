import uvicorn
from fastapi import FastAPI

from database import engine, Base

app = FastAPI()

Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    uvicorn.run("main:app",
                host="0.0.0.0",
                port=5000,
                log_level="info",
                reload=True)
