import cv2 as cv
import os
from train_recognizer import *

present = []  # List to store names of detected people

def test_recognizer():
    recognizer = cv.face.LBPHFaceRecognizer_create()
    recognizer.read('face_recognizer.yml')  # Load the trained recognizer model

    # Initialize video capture (webcam)
    capture = cv.VideoCapture(0)

    # Load Haar Cascade for face detection
    face_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_default.xml')

    while True:
        isTrue, frame = capture.read()  # Read a frame from the webcam
        if not isTrue:
            print("Error accessing the webcam.")
            break

        # Convert the frame to grayscale
        gray_test = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

        # Detect faces in the frame
        faces = face_cascade.detectMultiScale(gray_test, scaleFactor=1.3, minNeighbors=6)

        for (x, y, w, h) in faces:
            # Extract the region of interest (ROI) for face prediction
            roi_gray = gray_test[y:y+h, x:x+w]

            try:
                label, confidence = recognizer.predict(roi_gray)
                if confidence > 100:  # Threshold for unrecognized faces
                    name_without_extension = "Not Recognized"
                else:
                    image_name = image_files[label]  # Get the image file name using the label
                    name_without_extension = os.path.splitext(os.path.basename(image_name))[0]  # Extract name without extension
                    
                    # Add to 'present' only if not already added
                    
                    present.append(name_without_extension)
                    print(f"{name_without_extension} marked present")
                    # Draw rectangle and display "Marked Present"
                    cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                    cv.putText(frame, f"{name_without_extension} - Marked Present", (x, y - 10), 
                               cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
                    # Pause for a short duration to display the message
                    cv.imshow('Detected Faces', frame)
                    cv.waitKey(2000)  # Pause for 2 seconds to show text
                    break  # Move to the next frame after marking

            except Exception as e:
                print(f"Error predicting face: {e}")
                continue

        # Show the live frame continuously
        cv.imshow('Detected Faces', frame)

        # Exit on 'd' key press
        if cv.waitKey(1) & 0xFF == ord('d'):
            break

    # Release the capture object and close all OpenCV windows
    capture.release()
    cv.destroyAllWindows()

    # Print all detected people
    print("People marked present:", present)

test_recognizer()
