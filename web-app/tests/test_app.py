
"""Tests for the Flask starter application."""
from app import app

def test_homepage():
    """Check that the homepage loads successfully."""
    app.config["TESTING"] = True

    with app.test_client() as client:
        response = client.get("/")

    assert response.status_code == 200
    assert b"Simon Says Camera Challenge" in response.data
