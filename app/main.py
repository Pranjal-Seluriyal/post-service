from fastapi import FastAPI

from app.database.database import Base, engine

# Import models so SQLAlchemy creates tables
from app.models.user import User
from app.models.post import Post
from app.models.like import Like
from app.models.comment import Comment
from app.models.bookmark import Bookmark

from app.api.auth import router as auth_router
from app.api.users import router as users_router
from app.api.posts import router as posts_router
from app.api.likes import router as likes_router
from app.api.comments import router as comments_router
from app.api.bookmarks import router as bookmarks_router

Base.metadata.create_all(bind=engine)

# app = FastAPI(
#     title="Post Service API",
#     version="1.0.0",
# )
app = FastAPI(
    title="Post Service API",
    description="""
A RESTful social media backend built using FastAPI.

## Features

- JWT Authentication
- User Registration & Login
- CRUD Posts
- Like & Unlike Posts
- Comments
- Bookmarks
- Search Posts
- Pagination

Built by Pranjal Seluriyal.
""",
    version="1.0.0",
)
app.include_router(auth_router)
app.include_router(users_router)
app.include_router(posts_router)
app.include_router(likes_router)
app.include_router(comments_router)
app.include_router(bookmarks_router)


@app.get("/")
def home():
    return {
        "message": "Post Service Running"
    }