from pydantic import BaseModel 
from pydantic import EmailStr

class UserCreate(BaseModel):
    email: EmailStr
    username: str
    password: str

class UserResponse(BaseModel):
    id: int 
    email: str
    username: str

    model_config = {
        "from_attributes": True
    }
