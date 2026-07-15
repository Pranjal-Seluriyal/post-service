from fastapi import FastAPI

from app.api.posts import router as post_router

from app.database.database import Base
from app.database.database import engine

from app.models.post import Post

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Post Service API")


@app.get("/")
def home():
    return {"message": "Post Service API is Running 🚀"}


app.include_router(post_router)