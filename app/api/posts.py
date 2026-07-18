from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.core.security import get_current_user
from app.models.user import User
from app.schemas.post import (
    PostCreate,
    PostUpdate,
    PostResponse,
)
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


# @router.get("/", response_model=list[PostResponse])
# def read_posts(
#     db: Session = Depends(get_db),
# ):
#     return get_all_posts(db)
@router.get("/", response_model=list[PostResponse])
def read_posts(
    search: str = "",
    page: int = 1,
    limit: int = 10,
    db: Session = Depends(get_db),
):
    return get_all_posts(
        db=db,
        search=search,
        page=page,
        limit=limit,
    )


@router.get("/{post_id}", response_model=PostResponse)
def read_post(
    post_id: int,
    db: Session = Depends(get_db),
):
    post = get_post_by_id(db, post_id)

    if post is None:
        raise HTTPException(
            status_code=404,
            detail="Post not found",
        )

    return post


@router.post("/", response_model=PostResponse)
def add_post(
    post: PostCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return create_post(
        db,
        post,
        current_user,
    )


@router.put("/{post_id}", response_model=PostResponse)
def edit_post(
    post_id: int,
    post: PostUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    updated = update_post(
        db,
        post_id,
        post,
        current_user,
    )

    if updated is None:
        raise HTTPException(
            status_code=404,
            detail="Post not found",
        )

    if updated == "forbidden":
        raise HTTPException(
            status_code=403,
            detail="You can edit only your own posts",
        )

    return updated


@router.delete("/{post_id}")
def remove_post(
    post_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    deleted = delete_post(
        db,
        post_id,
        current_user,
    )

    if deleted is None:
        raise HTTPException(
            status_code=404,
            detail="Post not found",
        )

    if deleted == "forbidden":
        raise HTTPException(
            status_code=403,
            detail="You can delete only your own posts",
        )

    return {
        "message": "Post deleted successfully"
    }