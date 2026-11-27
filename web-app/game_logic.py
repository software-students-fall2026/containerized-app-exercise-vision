import random 
GESTURES = [
    "open_palm",
    "fist",
    "thumbs_up",
    "peace_sign",
    "pointing",
    "finger_gun",
    "rock_horns",
    "three_fingers",
    "shaka",
    "pinky_up",
]

class Game():
    def __init__(self):
        self.score = 0
        self.streak = 0
    def instruction():
        prefix = "Simon says: " if random.randint(1,2) == 1 else ""
        gesture = GESTURES[random.randint([range(len(GESTURES))])]
        return prefix + gesture

    def score_gesture(instruction: str, detected_gesture: str):
        gesture = [g for g in GESTURES if g in instruction][0]
        gesture_valid = gesture == detected_gesture or "Simon says" in instruction
        if gesture_valid: 
            self.score += 1
            self.streak += 1
        else: 
            self.streak = 0
            return "Game over"

            