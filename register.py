import cv2 as cv
import os
import time

def register():
    # Create/Open the video capture for the webcam
    capture = cv.VideoCapture(0)

    print("Press 'Space' to capture the photo or 'q' to quit.")
    frame = None
    while True:
        isTrue, frame = capture.read()  # Read a frame from the webcam

        if not isTrue:
            print("Error: Unable to read frame.")
            break

        # Display the live feed with instructions
        font = cv.FONT_HERSHEY_SIMPLEX
        cv.putText(frame, 'Press Space to Capture or q to Quit', (10, 30), font, 0.8, (0, 255, 0), 2, cv.LINE_AA)
        cv.imshow("Register - Webcam", frame)

        # Wait for user input to capture or quit
        key = cv.waitKey(20)
        if key & 0xFF == ord(' '):  # Space key to capture
            print("Photo captured.")
            capture.release()
            cv.destroyAllWindows()
            break
        elif key & 0xFF == ord('q'):  # 'q' to quit
            print("Quitting registration.")
            capture.release()
            cv.destroyAllWindows()
            return

    if frame is not None:  # Check if a frame was successfully captured
        # Ask for the user's name
        user_name = input("Enter the name of the person: ").strip()

        # Create a folder if it doesn't exist
        folder = "photos"
        try:
            if not os.path.exists(folder):
                os.makedirs(folder)
        except Exception as e:
            print(f"Error creating folder: {e}")
            capture.release()
            cv.destroyAllWindows()
            return

        # Save the captured photo with a unique filename (based on time)
        file_path = os.path.join(folder, f"{user_name}.jpg")
        cv.imwrite(file_path, frame)

        print(f"Photo saved successfully as {file_path}")
    else:
        print("No frame captured. Registration aborted.")

    # Release resources
    capture.release()
    cv.destroyAllWindows()

