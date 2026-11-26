"""Tests for hand gesture recognition."""

from types import SimpleNamespace
import numpy as np
from gesture_detector import (
    classify_gesture,
    detect_hand,
    recognize_gesture,
)


def create_landmarks(fingers, thumb=False):
    """Create sample landmarks for testing finger positions."""
    landmarks = [SimpleNamespace(x=0.0, y=0.0, z=0.0) for _ in range(21)]

    fingertips = [8, 12, 16, 20]
    finger_joints = [6, 10, 14, 18]

    for tip, joint, extended in zip(fingertips, finger_joints, fingers):
        landmarks[joint].y = 0.5

        if extended:
            landmarks[tip].y = 0.8
        else:
            landmarks[tip].y = 0.3

    landmarks[5].x = 0.2
    landmarks[17].x = -0.2

    if thumb:
        landmarks[4].x = 0.6
    else:
        landmarks[4].x = 0.1

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
    landmarks = create_landmarks([False, True, True, False])
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


def test_pointing():
    """Check pointing gesture classification."""
    landmarks = create_landmarks([True, False, False, False])
    assert classify_gesture(landmarks) == "pointing"


def test_rock_horns():
    """Check rock horns classification."""
    landmarks = create_landmarks([True, False, False, True])
    assert classify_gesture(landmarks) == "rock_horns"


def test_three_fingers():
    """Check three fingers classification."""
    landmarks = create_landmarks([True, True, True, False])
    assert classify_gesture(landmarks) == "three_fingers"


def test_three_fingers_alternative():
    """Check alternative three-finger classification."""
    landmarks = create_landmarks([False, True, True, True])
    assert classify_gesture(landmarks) == "three_fingers"


def test_pinky_up():
    """Check pinky up classification."""
    landmarks = create_landmarks([False, False, False, True])
    assert classify_gesture(landmarks) == "pinky_up"


def test_thumbs_up():
    """Check thumbs up classification."""
    landmarks = create_landmarks([False, False, False, False], thumb=True)
    assert classify_gesture(landmarks) == "thumbs_up"


def test_finger_gun():
    """Check finger gun classification."""
    landmarks = create_landmarks([True, False, False, False], thumb=True)
    assert classify_gesture(landmarks) == "finger_gun"


def test_shaka():
    """Check hang loose classification."""
    landmarks = create_landmarks([False, False, False, True], thumb=True)
    assert classify_gesture(landmarks) == "shaka"
