# Simon Says Camera Challenge — Architecture

## Project Overview

Simon Says Camera Challenge is a webcam-based game
where players respond to commands using hand gestures.

The application will use three Docker containers:

1. Flask web application
2. Python machine-learning client
3. MongoDB database

## Web Application

Directory: web-app/

Responsibilities:
- Display the game interface.
- Capture webcam images using the browser.
- Communicate with the ML client.
- Display scores and game history.

## Machine-Learning Client

Directory: machine-learning-client/

Responsibilities:
- Analyze images from the webcam.
- Recognize hand gestures.
- Evaluate Simon Says commands.
- Store analysis results in MongoDB.

Initial gestures:
- Open palm
- Fist
- Peace sign

## MongoDB

Responsibilities:
- Store game results and timestamps.
- Store player scores and game history.
- Provide data for the Flask dashboard.

## Planned Communication

Browser -> Flask -> ML Client -> MongoDB

Flask will communicate with the ML client using HTTP.

The Flask dashboard will retrieve stored results
from MongoDB.

## Development Guidelines

- Each Python subsystem has its own Pipfile.
- Each subsystem has its own tests/ directory.
- Use feature branches and pull requests.
- All team members participate in code reviews.
- Both Python subsystems must achieve at least
  80% automated test coverage.
- Docker Compose will eventually run all three services.

## Current Status

Completed:
- Initial folder structure
- Flask homepage
- ML client entry point
- Initial automated tests for both subsystems

Not yet implemented:
- Gesture recognition
- Game rules and scoring
- HTTP API communication
- MongoDB integration
- Docker configuration
- Full game interface and dashboard
