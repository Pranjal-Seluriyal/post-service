# Post Service

A production-oriented **Post Microservice** for a social media platform, responsible for creating, managing, and serving user-generated content and its interactions.

The service is designed as an **independently deployable backend service**. It owns its own PostgreSQL database and exposes a REST API that other services communicate with over HTTP.

---

## Overview

The Post Service manages the complete lifecycle of social media posts and their associated engagement.

It provides APIs for:

- Posts
- Comments and replies
- Likes
- Saves / bookmarks
- Shares
- Media metadata
- Hashtags
- Mentions
- Engagement counters
- Personalized feed retrieval
- Post visibility and moderation status
- JWT-based request authentication
- Health and readiness monitoring

The service is intentionally separated from authentication and user management.

### Responsibility Boundary

```text
                    Main Application
                           |
                           | HTTP / REST
                           v
                  +-------------------+
                  |    Post Service   |
                  +-------------------+
                    |       |       |
                    |       |       |
                    v       v       v
               PostgreSQL  Media   User Service
                           Storage   (optional)


✨ Features
📝 Post Management
Create posts
Retrieve posts
Retrieve individual posts
Update posts
Soft-delete posts
Post visibility
Post moderation/status
Post timestamps
Engagement counters
Media association
Hashtag association
Mention association

Comments & Replies
Create comments
Retrieve comments
Update comments
Delete comments
Nested replies
Parent-child comment relationships
Soft/deleted comment representation

Comments & Replies
Create comments
Retrieve comments
Update comments
Delete comments
Nested replies


Users can save posts for later.

Users can share posts.

The media system supports:

Images
Videos
Media metadata
Media ordering
MIME types
Storage keys/paths
Width
Height
Duration
Post-media relationships

Uploaded files are validated using multiple checks:

File extension validation
MIME type validation
File-size limits
File signature / magic-byte validation
Filename sanitization
Safe path handling
Path traversal protection
Allowed media type validation

The service supports hashtags in posts.
The service supports user mentions inside post content.

The service provides feed retrieval:

GET /api/v1/feed/

Feed functionality includes:

Post ordering
Pagination
Cursor-based pagination
Offset pagination
Media loading
Engagement information

The feed has its own service and repository layer instead of putting feed logic directly into post CRUD.

JWT validation includes:

Signature validation
Expiration validation
User identity extraction
Required claim validation

The Post Service does not manage:

Passwords
Login
Signup
User credentials

post-service/
│
├── app/
│   │
│   ├── api/
│   │   ├── routes/
│   │   │   ├── comments.py
│   │   │   ├── feed.py
│   │   │   ├── hashtags.py
│   │   │   ├── health.py
│   │   │   ├── likes.py
│   │   │   ├── media.py
│   │   │   ├── posts.py
│   │   │   ├── saves.py
│   │   │   └── shares.py
│   │   │
│   │   ├── dependencies.py
│   │   └── health.py
│   │
│   ├── core/
│   │   ├── config.py
│   │   ├── logging.py
│   │   └── security.py
│   │
│   ├── database/
│   │   └── database.py
│   │
│   ├── integrations/
│   │   ├── storage.py
│   │   └── user_client.py
│   │
│   ├── models/
│   │   ├── bookmark.py
│   │   ├── comment.py
│   │   ├── hashtag.py
│   │   ├── like.py
│   │   ├── media.py
│   │   ├── mention.py
│   │   ├── post.py
│   │   ├── save.py
│   │   ├── share.py
│   │   └── user.py
│   │
│   ├── repositories/
│   │   ├── bookmark_repository.py
│   │   ├── comment_repository.py
│   │   ├── feed_repository.py
│   │   ├── hashtag_repository.py
│   │   ├── like_repository.py
│   │   ├── media_repository.py
│   │   ├── post_repository.py
│   │   ├── save_repository.py
│   │   └── share_repository.py
│   │
│   ├── schemas/
│   │   ├── comment.py
│   │   ├── engagement.py
│   │   ├── feed.py
│   │   ├── hashtag.py
│   │   ├── media.py
│   │   ├── post.py
│   │   └── share.py
│   │
│   └── services/
│       ├── bookmark_service.py
│       ├── comment_service.py
│       ├── engagement_service.py
│       ├── feed_service.py
│       ├── hashtag_service.py
│       ├── like_service.py
│       ├── media_service.py
│       ├── post_service.py
│       ├── save_service.py
│       └── share_service.py
│
├── alembic/
│   ├── env.py
│   ├── script.py.mako
│   └── versions/
│       └── 001_initial_schema.py
│
├── tests/
│   ├── conftest.py
│   ├── test_comments.py
│   ├── test_engagement.py
│   ├── test_feed.py
│   ├── test_hashtags.py
│   ├── test_health.py
│   ├── test_interactions.py
│   ├── test_likes.py
│   ├── test_media.py
│   ├── test_media_security.py
│   ├── test_posts.py
│   ├── test_saves.py
│   ├── test_shares.py
│   ├── test_transaction_rollback.py
│   └── test_workflow.py
│
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── Dockerfile
├── docker-compose.yml
├── docker-entrypoint.sh
├── alembic.ini
├── requirements.txt
├── .env.example
├── .dockerignore
├── .gitignore
├── INTEGRATION.md
└── README.md

