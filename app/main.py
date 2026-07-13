from fastapi import FastAPI

from app.api.posts import router as post_router

app = FastAPI(title="Post Service API")


@app.get("/")
def home():
    return {"message": "Post Service API is Running 🚀"}


app.include_router(post_router)