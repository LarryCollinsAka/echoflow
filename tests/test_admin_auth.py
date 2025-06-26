import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.database import SessionLocal
from app.models import User
from app.auth import hash_password

client = TestClient(app)

# Utility to create a user in the test database
def create_user(username, email, password, role):
    db = SessionLocal()
    # Clean up any existing user
    db.query(User).filter((User.username == username) | (User.email == email)).delete()
    db.commit()
    user = User(
        username=username,
        email=email,
        password_hash=hash_password(password),
        role=role
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    db.close()
    return user

@pytest.fixture(scope="module")
def admin_user():
    return create_user("adminuser", "admin@example.com", "adminpass", "admin")

@pytest.fixture(scope="module")
def normal_user():
    return create_user("normaluser", "user@example.com", "userpass", "ngo")

def get_token(username, password):
    response = client.post("/login", data={
        "username": username,
        "password": password
    })
    assert response.status_code == 200
    return response.json()["access_token"]

def test_admin_access(admin_user):
    token = get_token("adminuser", "adminpass")
    headers = {"Authorization": f"Bearer {token}"}
    response = client.get("/admin/dashboard", headers=headers)
    assert response.status_code == 200
    assert "Welcome" in response.text

def test_non_admin_access(normal_user):
    token = get_token("normaluser", "userpass")
    headers = {"Authorization": f"Bearer {token}"}
    response = client.get("/admin/dashboard", headers=headers)
    assert response.status_code == 403
    assert "not permitted" in response.text or "forbidden" in response.text

def test_admin_dashboard_requires_auth():
    response = client.get("/admin/dashboard")
    assert response.status_code == 401 or response.status_code == 403