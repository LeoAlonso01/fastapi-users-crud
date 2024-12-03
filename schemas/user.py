# Description: User schema for pydantic
from typing import Optional
from pydantic import BaseModel

class User(BaseModel):
    id: Optional[str]
    username: Optional[str]
    email: Optional[str]
    password: Optional[str]
    is_active: Optional[bool]