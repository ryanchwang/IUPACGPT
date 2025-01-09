import cv2
import numpy as np
import matplotlib.pyplot as plt


def preprocess_image(image_path, output_path):
    # Load the image from the file path
    image = cv2.imread(image_path)
    
    # Resize the image to 500x500 pixels
    image = cv2.resize(image, (500, 500))
    
    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Apply a bilateral filter to reduce noise and keep edges sharp
    filtered_image = cv2.bilateralFilter(gray_image, d=9, sigmaColor=75, sigmaSpace=75)
    
    # Use Canny edge detector to detect edges in the image
    edges = cv2.Canny(filtered_image, threshold1=50, threshold2=150)
    
    # Save the final image with edges detected
    cv2.imwrite(output_path, edges)
    
    # Optionally display the final image
    cv2.imshow('Final Processed Image', edges)
    cv2.waitKey(0)
    cv2.destroyAllWindows()