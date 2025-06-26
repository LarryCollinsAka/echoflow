import uuid
from pydantic import BaseModel, EmailStr, Field
from app.enums import UserRole, MeetingStatus

class LoginRequest(BaseModel):
    email: EmailStr
    password: str

# Shared properties
class UserBase(BaseModel):
    username: str
    email: EmailStr
    full_name: str | None = None
    role: UserRole = UserRole.PERSONAL

# Properties to receive on user creation
class UserCreate(UserBase):
    password: str = Field(..., min_length=8)

# Properties to return to client
class UserRead(UserBase):
    id: uuid.UUID

class Config:
    from_attributes = True

# Meeting schemas
class MeetingBase(BaseModel):
    title: str
    scheduled_time: str  # You may want to use datetime later
    status: MeetingStatus = MeetingStatus.SCHEDULED

class MeetingCreate(MeetingBase):
    pass

class MeetingRead(MeetingBase):
    id: uuid.UUID
    user_id: uuid.UUID

    class Config:
        orm_mode = True