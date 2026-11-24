"""Hand gesture recognition for the Simon Says game."""

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


def classify_gesture(landmarks):
    """Classify a gesture using finger landmark positions."""
    fingertips = [8, 12, 16, 20]
    finger_joints = [6, 10, 14, 18]

    fingers = []

    for tip, joint in zip(fingertips, finger_joints):
        fingers.append(landmarks[tip].y < landmarks[joint].y)

    if fingers == [True, True, True, True]:
        return "open_palm"

    if fingers == [False, False, False, False]:
        return "fist"

    if fingers == [True, True, False, False]:
        return "peace_sign"

    return "unknown"


def recognize_gesture(image):
    """Detect a hand and return its recognized gesture."""
    landmarks = get_landmarks(image)

    if landmarks is None:
        return "no_hand"

    return classify_gesture(landmarks)
