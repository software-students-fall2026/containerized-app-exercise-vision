"""API for the Simon Says machine learning client."""

import cv2
import numpy as np
from flask import Flask, request, jsonify

from gesture_detector import recognize_gesture

app = Flask(__name__)


@app.route("/recognize", methods=["POST"])
def recognize():
    """Receive an image and return its recognized gesture."""
    if "image" not in request.files:
        return jsonify({"error": "No image provided"}), 400

    image_file = request.files["image"]
    image_data = np.frombuffer(image_file.read(), dtype=np.uint8)

    if image_data.size == 0:
        return jsonify({"error": "Invalid image"}), 400

    # pylint: disable-next=no-member
    image = cv2.imdecode(image_data, cv2.IMREAD_COLOR)

    if image is None:
        return jsonify({"error": "Invalid image"}), 400

    gesture = recognize_gesture(image)

    return jsonify({"gesture": gesture})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
