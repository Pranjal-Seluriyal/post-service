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
