#Made by Riza Mohamed T
import cv2
import cvzone
from cvzone.FaceMeshModule import FaceMeshDetector

# Initialize the webcam capture
cap = cv2.VideoCapture(0)

# Create a FaceMeshDetector object with a maximum of 1 face to detect
detector = FaceMeshDetector(maxFaces=1)

while True:
    # Read a frame from the webcam
    success, img = cap.read()

    # Detect face mesh in the image
    img, faces = detector.findFaceMesh(img, draw=False)

    # If faces are detected
    if faces:
        face = faces[0]  # Take the first detected face

        # Get specific points on the face mesh for depth calculation
        pointLeft = face[145]  # A point on the left side of the face
        pointRight = face[374]  # A point on the right side of the face

        # Calculate the width of the face in pixels
        w, _ = detector.findDistance(pointLeft, pointRight)

        # Known width of the face in centimeters
        W = 6.3

        # Known focal length of the camera
        f = 840

        # Calculate the depth using the formula: depth = (width * focal_length) / known_width
        d = (W * f) / w

        # Print the calculated depth
        print(d)

        # Display the depth on the image
        cvzone.putTextRect(img, f'Depth: {int(d)}cm', (face[10][0] - 100, face[10][1] - 50), scale=2)

    # Display the annotated image
    cv2.imshow("Image", img)

    # Wait for a key press and check for termination
    if cv2.waitKey(1) & 0xFF == 27:  # Press 'Esc' key to exit
        break

# Release the webcam and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
