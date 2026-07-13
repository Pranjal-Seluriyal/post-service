from app.database.fake_db import posts


def get_all_posts():
    return posts


def get_post_by_id(post_id: int):
    for post in posts:
        if post["id"] == post_id:
            return post
    return None


def create_post(post):
    post_dict = post.model_dump()
    post_dict["id"] = len(posts) + 1

    posts.append(post_dict)

    return post_dict


def update_post(post_id: int, updated_post):
    for index, post in enumerate(posts):
        if post["id"] == post_id:
            updated_dict = updated_post.model_dump()
            updated_dict["id"] = post_id
            posts[index] = updated_dict
            return updated_dict

    return None


def delete_post(post_id: int):
    for index, post in enumerate(posts):
        if post["id"] == post_id:
            deleted = posts.pop(index)
            return deleted

    return None