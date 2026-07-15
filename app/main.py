from fastapi import FastAPI

from app.api.posts import router as post_router
from app.api.auth import router as auth_router

from app.database.database import Base, engine

# Import models so SQLAlchemy creates their tables
from app.models.post import Post
from app.models.user import User

# Create database tables
Base.metadata.create_all(bind=engine)

# Create FastAPI app
app = FastAPI(title="Post Service API")


@app.get("/")
def home():
    return {
        "message": "Post Service API is Running 🚀"
    }


# Register routers
app.include_router(auth_router)
app.include_router(post_router)