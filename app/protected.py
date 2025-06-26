from fastapi import APIRouter, Depends
from app.models import User
from app.deps import get_current_user

router = APIRouter()

@router.get("/profile")
def read_profile(current_user: User = Depends(get_current_user)):
    return {
        "id": str(current_user.id),
        "username": current_user.username,
        "email": current_user.email,
        "role": current_user.role.value,
    }