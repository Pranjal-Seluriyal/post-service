from sqlalchemy.orm import Session

from app.models.post import Post
from app.schemas.post import PostCreate


def get_all_posts(db: Session):
    return db.query(Post).all()


def get_post_by_id(db: Session, post_id: int):
    return db.query(Post).filter(Post.id == post_id).first()


def create_post(db: Session, post: PostCreate):
    db_post = Post(
        title=post.title,
        content=post.content,
        author=post.author,
    )

    db.add(db_post)
    db.commit()
    db.refresh(db_post)

    return db_post


def update_post(db: Session, post_id: int, post: PostCreate):
    db_post = db.query(Post).filter(Post.id == post_id).first()

    if db_post is None:
        return None

    db_post.title = post.title
    db_post.content = post.content
    db_post.author = post.author

    db.commit()
    db.refresh(db_post)

    return db_post


def delete_post(db: Session, post_id: int):
    db_post = db.query(Post).filter(Post.id == post_id).first()

    if db_post is None:
        return None

    db.delete(db_post)
    db.commit()

    return db_post