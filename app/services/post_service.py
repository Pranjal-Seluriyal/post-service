from sqlalchemy.orm import Session

from app.models.post import Post
from app.models.user import User
from app.schemas.post import PostCreate, PostUpdate

from sqlalchemy import or_

def get_all_posts(
    db: Session,
    search: str = "",
    page: int = 1,
    limit: int = 10,
):
    query = db.query(Post)

    if search:
        query = query.filter(
            or_(
                Post.title.ilike(f"%{search}%"),
                Post.content.ilike(f"%{search}%"),
            )
        )

    return (
        query.order_by(Post.id.desc())
        .offset((page - 1) * limit)
        .limit(limit)
        .all()
    )
# def get_all_posts(db: Session):
#     return db.query(Post).order_by(Post.id.desc()).all()


def get_post_by_id(db: Session, post_id: int):
    return db.query(Post).filter(Post.id == post_id).first()


def create_post(
    db: Session,
    post: PostCreate,
    current_user: User,
):
    db_post = Post(
        title=post.title,
        content=post.content,
        author_id=current_user.id,
    )

    db.add(db_post)
    db.commit()
    db.refresh(db_post)

    return db_post


def update_post(
    db: Session,
    post_id: int,
    post: PostUpdate,
    current_user: User,
):
    db_post = db.query(Post).filter(Post.id == post_id).first()

    if db_post is None:
        return None

    if db_post.author_id != current_user.id:
        return "forbidden"

    if post.title is not None:
        db_post.title = post.title

    if post.content is not None:
        db_post.content = post.content

    db.commit()
    db.refresh(db_post)

    return db_post


def delete_post(
    db: Session,
    post_id: int,
    current_user: User,
):
    db_post = db.query(Post).filter(Post.id == post_id).first()

    if db_post is None:
        return None

    if db_post.author_id != current_user.id:
        return "forbidden"

    db.delete(db_post)
    db.commit()

    return True