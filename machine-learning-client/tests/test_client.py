"""Tests for the machine learning client API."""

from io import BytesIO
import cv2
import numpy as np
from client import app


def test_missing_image():
    """Check requests without an image."""
    with app.test_client() as client:
        response = client.post("/recognize")

    assert response.status_code == 400
    assert response.get_json() == {"error": "No image provided"}


def test_invalid_image():
    """Check requests containing invalid image data."""
    data = {"image": (BytesIO(b"invalid image"), "test.jpg")}

    with app.test_client() as client:
        response = client.post("/recognize", data=data)

    assert response.status_code == 400
    assert response.get_json() == {"error": "Invalid image"}


def test_empty_image():
    """Check requests containing an empty image file."""
    data = {"image": (BytesIO(b""), "test.jpg")}

    with app.test_client() as client:
        response = client.post("/recognize", data=data)

    assert response.status_code == 400
    assert response.get_json() == {"error": "Invalid image"}


def test_valid_image():
    """Check recognition of a valid image without a hand."""
    image = np.zeros((480, 640, 3), dtype=np.uint8)

    # pylint: disable-next=no-member
    success, encoded_image = cv2.imencode(".jpg", image)
    assert success

    data = {"image": (BytesIO(encoded_image.tobytes()), "test.jpg")}

    with app.test_client() as client:
        response = client.post("/recognize", data=data)

    assert response.status_code == 200
    assert response.get_json() == {"gesture": "no_hand"}
