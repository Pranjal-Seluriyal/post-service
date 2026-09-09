# Note: In accordance with microservice database boundaries, 
# Post Service does NOT own or maintain a local 'users' database table.
# User identities are established via JWT tokens and integrated via API boundaries.

from pydantic import BaseModel


class User(BaseModel):
    id: int
    username: str
    email: str

    model_config = {
        "from_attributes": True
    }