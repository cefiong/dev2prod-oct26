import pytest
import requests
import time

BASE_URL = "http://127.0.0.1:5001/api"

def test_health_check():
    # Arrange and Act
    response = requests.get(f"{BASE_URL}/health")

    # Assert
    # check status code
    assert response.status_code == 200

    # check the retured data
    assert response.json()["status"] == "healthy"

def test_user_registration():
    # create a unique user
    username = f"user_{time.time() * 1000}"
    user = {
        "username": username,
        "password": "pass123"
    }

    response = requests.post(f"{BASE_URL}/auth/register", json=user)

    # Assert
    assert response.status_code == 201

    assert response.json()["message"] == "User created successfully"

    assert response.json()["user"]["username"] == user["username"]

    assert response.status_code != 401


def test_create_poll(auth_token):
    """Test creating a public poll"""
    # Arrange: Poll data
    poll_data = {
        "question": "What is your favorite language?",
        "options": ["Python", "JavaScript", "Java"],
        "is_public": True,
        "requires_admin": False
    }

    # Act: Create poll
    headers = {"Authorization": f"Bearer {auth_token}"}
    response = requests.post(
        f"{BASE_URL}/polls",
        json=poll_data,
        headers=headers
    )

    # Assert: Check response
    assert response.status_code == 201
    data = response.json()
    assert data["question"] == poll_data["question"]
    assert data["is_public"] == True
    assert len(data["options"]) == 3
    assert "id" in data

