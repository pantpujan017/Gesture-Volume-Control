# Hand Tracking and Volume Control

This project utilizes Python with OpenCV and Mediapipe to track hand gestures in real-time. It enables users to control the system volume by detecting specific hand movements, specifically using finger positions.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [How It Works](#how-it-works)
- [Contributing](#contributing)
- [License](#license)

## Installation

To run this project on your local machine, follow these steps:

1. Clone the repository:
git clone https://github.com/pantpujan017/Gesture-Volume-Control.git

2. Navigate to the project directory:
cd Gesture-Volume-Control

3. Install dependencies using pip:
pip install -r requirements.txt


## Usage

1. Ensure your webcam is connected and accessible.
2. Run the application using Python:
3. Position your hand in front of the camera to initiate hand tracking.
4. Control the system volume using the following gestures:
- Move your pinky finger up to increase the volume.
- Move your pinky finger down to decrease the volume.
5. The current volume level is displayed visually on the screen.

## Features

- Real-time hand tracking using OpenCV and Mediapipe.
- Detection of finger positions to control system volume.
- Visual feedback for volume level and finger positions.

## How It Works

This project uses computer vision techniques to detect and track landmarks on the hand, specifically focusing on the index finger and thumb for controlling volume. The application calculates the distance between these landmarks in real-time and maps this distance to adjust the system volume accordingly. Visual indicators on the screen provide feedback to the user about the current volume level.

## Contributing

Contributions to this project are welcome and encouraged! If you want to contribute to the project, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Create a new Pull Request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.


