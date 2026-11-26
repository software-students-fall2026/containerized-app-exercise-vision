"""Hand gesture recognition for the Simon Says game."""

import math

import cv2
import mediapipe as mp


def get_landmarks(image):
    """Return hand landmarks if a hand is detected."""
    if image is None:
        return None

    hands_module = mp.solutions.hands

    with hands_module.Hands(
        static_image_mode=True,
        max_num_hands=1,
        min_detection_confidence=0.5,
    ) as hands:
        # pylint: disable-next=no-member
        rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = hands.process(rgb_image)

    if not results.multi_hand_landmarks:
        return None

    return results.multi_hand_landmarks[0].landmark


def detect_hand(image):
    """Return True if a hand is detected."""
    return get_landmarks(image) is not None


def landmark_distance(first, second):
    """Calculate the distance between two hand landmarks."""
    return math.sqrt(
        (first.x - second.x) ** 2
        + (first.y - second.y) ** 2
        + (first.z - second.z) ** 2
    )


def is_finger_extended(landmarks, tip, joint):
    """Determine whether a finger is extended."""
    wrist = landmarks[0]

    tip_distance = landmark_distance(landmarks[tip], wrist)
    joint_distance = landmark_distance(landmarks[joint], wrist)

    return tip_distance > joint_distance * 1.2


def is_thumb_extended(landmarks):
    """Determine whether the thumb is extended."""
    thumb_distance = landmark_distance(landmarks[4], landmarks[17])
    palm_width = landmark_distance(landmarks[5], landmarks[17])

    return thumb_distance > palm_width * 1.5


def classify_gesture(landmarks):
    """Classify a gesture using hand landmark positions."""
    fingertips = [8, 12, 16, 20]
    finger_joints = [6, 10, 14, 18]

    fingers = []

    for tip, joint in zip(fingertips, finger_joints):
        fingers.append(is_finger_extended(landmarks, tip, joint))

    thumb = is_thumb_extended(landmarks)

    gestures = {
        (True, True, True, True): "open_palm",
        (False, False, False, False): "thumbs_up" if thumb else "fist",
        (True, True, False, False): "peace_sign",
        (True, False, False, False): "finger_gun" if thumb else "pointing",
        (True, False, False, True): "rock_horns",
        (True, True, True, False): "three_fingers",
        (False, True, True, True): "three_fingers",
        (False, False, False, True): "shaka" if thumb else "pinky_up",
    }

    return gestures.get(tuple(fingers), "unknown")


def recognize_gesture(image):
    """Detect a hand and return its recognized gesture."""
    landmarks = get_landmarks(image)

    if landmarks is None:
        return "no_hand"

    return classify_gesture(landmarks)
