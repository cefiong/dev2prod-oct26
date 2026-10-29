import pytest
import models

def test_user_function():
    # Arrange
    user = models.User(username="user1")
    user.set_password("pass123")

    # Acts and Assert

    # Check if the password is OK
    assert user.check_password("pass123") == True

    # Check that the password is hashed
    assert user.password_hash != "pass123"