"""Tests for hand gesture recognition."""

from types import SimpleNamespace
import numpy as np
from gesture_detector import (
    classify_gesture,
    detect_hand,
    recognize_gesture,
)


def create_landmarks(fingers):
    """Create sample landmarks for testing finger positions."""
    landmarks = [SimpleNamespace(y=0.5) for _ in range(21)]
    fingertips = [8, 12, 16, 20]

    for tip, extended in zip(fingertips, fingers):
        if extended:
            landmarks[tip].y = 0.2
        else:
            landmarks[tip].y = 0.8

    return landmarks


def test_open_palm():
    """Check open palm classification."""
    landmarks = create_landmarks([True, True, True, True])
    assert classify_gesture(landmarks) == "open_palm"


def test_fist():
    """Check fist classification."""
    landmarks = create_landmarks([False, False, False, False])
    assert classify_gesture(landmarks) == "fist"


def test_peace_sign():
    """Check peace sign classification."""
    landmarks = create_landmarks([True, True, False, False])
    assert classify_gesture(landmarks) == "peace_sign"


def test_unknown_gesture():
    """Check unsupported gesture classification."""
    landmarks = create_landmarks([True, False, False, False])
    assert classify_gesture(landmarks) == "unknown"


def test_detect_hand_invalid_image():
    """Check hand detection without an image."""
    assert detect_hand(None) is False


def test_recognize_invalid_image():
    """Check gesture recognition without an image."""
    assert recognize_gesture(None) == "no_hand"


def test_detect_hand_blank_image():
    """Check hand detection on an image without a hand."""
    image = np.zeros((480, 640, 3), dtype=np.uint8)
    assert detect_hand(image) is False


def test_recognize_blank_image():
    """Check gesture recognition on an image without a hand."""
    image = np.zeros((480, 640, 3), dtype=np.uint8)
    assert recognize_gesture(image) == "no_hand"
