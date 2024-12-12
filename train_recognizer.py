import cv2 as cv
import os
import numpy as np

# Initialize empty lists to store images and labels
images = []
labels = []
image_files = []  # List to store image file names

# Function to prepare images and labels
def prepare_images():
    folder_path = 'photos'  # Path to the folder containing images
    for f in os.listdir(folder_path):
        if f.endswith(('.jpg', '.png')):
            image_files.append(f)

   

    current_label = 0  # Counter to assign unique labels

    for image_file in image_files:
        # Full path to the image file
        img_path = os.path.join(folder_path, image_file)
        
        # Read the image
        img = cv.imread(img_path)
        if img is None:
            print(f"Error: Image {img_path} not found!")
            continue
        
        gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)  # Convert image to grayscale
        
        images.append(gray)  # Add the grayscale image to the images list
        labels.append(current_label)  # Assign label
        current_label += 1  # Increment the label for the next image
    print("image successfully prepreared")
    
# Function to train the recognizer
def train_recognizer():
    recognizer = cv.face.LBPHFaceRecognizer_create()

    # Train the recognizer with the images and corresponding labels
    recognizer.train(images, np.asarray(labels))

    # Save the trained model to a file
    recognizer.save('face_recognizer.yml')
    print("Model trained and saved as 'face_recognizer.yml'")
