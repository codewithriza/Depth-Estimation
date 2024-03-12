# Depth Estimation from Face Width using OpenCV and FaceMesh

This Python script utilizes the OpenCV library along with the FaceMesh detection module to estimate the depth of a human face from a webcam feed. The code captures video frames from the webcam, detects a face using FaceMesh, and calculates the depth of the face based on the width of the detected face in the image. The calculated depth is then displayed on the image frame in centimeters.

## Features

- **Real-time Depth Estimation:** Estimates the depth of a human face in real-time from a webcam feed.
- **Simple Implementation:** Easy-to-understand code with minimal dependencies.
- **Customizable:** Can be customized for different face widths and camera focal lengths.

## How It Works

1. **Initialize Webcam and Detector:** Initializes the webcam capture and creates a FaceMeshDetector object with a maximum of 1 face to detect.

2. **Read Frame and Detect Face:** Reads a frame from the webcam, detects the face mesh, and calculates the width of the face.

3. **Calculate Depth:** Uses the known width of the face and the focal length of the camera to calculate the depth of the face.

4. **Display Depth:** Annotates the image frame with the calculated depth in centimeters and displays the annotated image.

5. **Terminate Script:** Terminates the script when the 'Esc' key is pressed.

## Setup

1. **Install Required Libraries:** Make sure you have the required libraries installed. You can install them using pip:
   ```bash
   pip install opencv-python cvzone
2. Run the Script: Run the Python script `main.py` . A window will open displaying the webcam feed with annotated depth information on the detected face.
   ```bash
   python3 main.py

## Notes
- Camera Calibration: Ensure that the camera is calibrated and the known focal length and face width are accurately provided for accurate depth estimation.

- Customization: The script can be customized for different camera setups and face sizes by adjusting the known face width (W) and focal length (f) values.

- Feel free to customize the script further for your specific needs.

## Contact Me

If you have any questions, suggestions, or issues with the script, feel free to contact me.

---
[![Discord](https://img.shields.io/badge/Discord-%235865F2.svg?style=for-the-badge&logo=discord&logoColor=white)](https://discord.com/users/887532157747212370)
[![X](https://img.shields.io/badge/X-%23000000.svg?style=for-the-badge&logo=X&logoColor=white)](https://twitter.com/codewithriza)
