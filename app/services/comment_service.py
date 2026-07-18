from sqlalchemy.orm import Session

from app.models.comment import Comment
from app.models.post import Post
from app.models.user import User


def add_comment(
    db: Session,
    post_id: int,
    content: str,
    current_user: User,
):
    post = db.query(Post).filter(Post.id == post_id).first()

    if post is None:
        return None

    comment = Comment(
        content=content,
        user_id=current_user.id,
        post_id=post_id,
    )

    db.add(comment)
    db.commit()
    db.refresh(comment)

    return comment


def get_comments(
    db: Session,
    post_id: int,
):
    return (
        db.query(Comment)
        .filter(Comment.post_id == post_id)
        .all()
    )


def delete_comment(
    db: Session,
    comment_id: int,
    current_user: User,
):
    comment = (
        db.query(Comment)
        .filter(Comment.id == comment_id)
        .first()
    )

    if comment is None:
        return None

    if comment.user_id != current_user.id:
        return "forbidden"

    db.delete(comment)
    db.commit()

    return True