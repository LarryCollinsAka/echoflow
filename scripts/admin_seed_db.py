from dotenv import load_dotenv
load_dotenv()

import uuid
from sqlalchemy.orm import Session
from app.models import User
from app.auth import hash_password
from settings import settings
from app.database import SessionLocal

def seed():
    db: Session = SessionLocal()
    try:
        email = "admin@echoflow.com"
        user = db.query(User).filter(User.email == email).first()
        if not user:
            print(f"Creating admin user: {email}")
            admin = User(
                id=uuid.uuid4(),
                username="admin",
                email=email,
                full_name="Admin User",
                password_hash=hash_password("adminpassword"),
                role="ADMIN",  # or use your Enum: UserRole.ADMIN
            )
            db.add(admin)
            db.commit()
            db.refresh(admin)
            print(f"Admin user created with email: {email} and password: adminpassword")
        else:
            print("Admin user already exists.")
    finally:
        db.close()

if __name__ == "__main__":
    seed()