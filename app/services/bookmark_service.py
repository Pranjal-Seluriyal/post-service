from sqlalchemy.orm import Session

from app.models.bookmark import Bookmark
from app.models.post import Post
from app.models.user import User


def add_bookmark(
    db: Session,
    post_id: int,
    current_user: User,
):
    post = db.query(Post).filter(Post.id == post_id).first()

    if post is None:
        return None

    existing = (
        db.query(Bookmark)
        .filter(
            Bookmark.user_id == current_user.id,
            Bookmark.post_id == post_id,
        )
        .first()
    )

    if existing:
        return "already"

    bookmark = Bookmark(
        user_id=current_user.id,
        post_id=post_id,
    )

    db.add(bookmark)
    db.commit()

    return True


def remove_bookmark(
    db: Session,
    post_id: int,
    current_user: User,
):
    bookmark = (
        db.query(Bookmark)
        .filter(
            Bookmark.user_id == current_user.id,
            Bookmark.post_id == post_id,
        )
        .first()
    )

    if bookmark is None:
        return None

    db.delete(bookmark)
    db.commit()

    return True


def my_bookmarks(
    db: Session,
    current_user: User,
):
    return (
        db.query(Bookmark)
        .filter(
            Bookmark.user_id == current_user.id
        )
        .all()
    )