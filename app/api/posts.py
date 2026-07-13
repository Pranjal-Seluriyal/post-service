from fastapi import APIRouter, HTTPException

from app.schemas.post import PostCreate
from app.services.post_service import (
    get_all_posts,
    get_post_by_id,
    create_post,
    update_post,
    delete_post,
)

router = APIRouter(
    prefix="/posts",
    tags=["Posts"],
)


@router.get("/")
def read_posts():
    return get_all_posts()


@router.get("/{post_id}")
def read_post(post_id: int):
    post = get_post_by_id(post_id)

    if post is None:
        raise HTTPException(
            status_code=404,
            detail="Post not found",
        )

    return post


@router.post("/")
def add_post(post: PostCreate):
    return create_post(post)


@router.put("/{post_id}")
def edit_post(post_id: int, post: PostCreate):
    updated = update_post(post_id, post)

    if updated is None:
        raise HTTPException(
            status_code=404,
            detail="Post not found",
        )

    return updated


@router.delete("/{post_id}")
def remove_post(post_id: int):
    deleted = delete_post(post_id)

    if deleted is None:
        raise HTTPException(
            status_code=404,
            detail="Post not found",
        )

    return {
        "message": "Post deleted successfully",
        "post": deleted,
    }