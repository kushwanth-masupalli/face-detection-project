import cv2 as cv
import os
import time
import pyautogui  # For simulating user interaction (if needed)
from train_recognizer import *

present = []  # List to store names of detected people
CONFIDENCE_THRESHOLD = 100  # Confidence threshold for face recognition
window = False  # Global variable to track if the window has been set up

def test_recognizer():
    global window  # Declare 'window' as a global variable to modify its value

    # Load the trained recognizer model
    recognizer = cv.face.LBPHFaceRecognizer_create()
    recognizer.read('face_recognizer.yml')

    # Initialize video capture (webcam)
    capture = cv.VideoCapture(0)
    if not capture.isOpened():
        print("Error: Unable to access the webcam.")
        return

    # Load Haar Cascade for face detection
    face_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_default.xml')

    while True:
        isTrue, frame = capture.read()  # Read a frame from the webcam
        if not isTrue:
            print("Error reading frame from webcam.")
            break

        # Convert the frame to grayscale
        gray_test = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

        # Detect faces in the frame
        faces = face_cascade.detectMultiScale(gray_test, scaleFactor=1.1, minNeighbors=5)

        for (x, y, w, h) in faces:
            # Extract the region of interest (ROI) for face prediction
            roi_gray = gray_test[y:y+h, x:x+w]

            try:
                label, confidence = recognizer.predict(roi_gray)
                if confidence > CONFIDENCE_THRESHOLD:  # Face not recognized
                    cv.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 3)
                    cv.putText(frame, "Not Recognized", (x, y - 10), cv.FONT_HERSHEY_COMPLEX, 1.0, (0, 0, 255), 2)
                else:  # Face recognized
                    if label < len(image_files):
                        image_name = image_files[label]
                        name_without_extension = os.path.splitext(os.path.basename(image_name))[0]
                        if name_without_extension not in present:
                            present.append(name_without_extension)
                            print(f"{name_without_extension} marked present")
                        cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)
                        cv.putText(frame, name_without_extension + " marked", (x - 50, y - 10),
                                   cv.FONT_HERSHEY_COMPLEX, 1.0, (0, 255, 0), 1)

            except Exception as e:
                print(f"Error predicting face: {e}")
                continue

        # Display the frame
        cv.imshow('Detected Faces', frame)

        if not window:
            # Set the OpenCV window as topmost
            cv.setWindowProperty('Detected Faces', cv.WND_PROP_TOPMOST, 1)
            
            # Add a delay to ensure the window is visible
            time.sleep(0.5)

            # Simulate clicks at four specific coordinates on the screen to activate the OpenCV window
            pyautogui.click(960, 540)  # Center of the screen
            pyautogui.click(480, 270)  # Top-left quarter
            pyautogui.click(1440, 810)  # Bottom-right quarter
            pyautogui.click(960, 810)  # Bottom-center

            window = True

        if cv.waitKey(20) & 0xFF == ord('k'):  # Single condition for exiting
            break

    # Release the capture object and close all OpenCV windows
    capture.release()
    cv.destroyAllWindows()

    # Print all detected people
    print("People marked present:", present)


