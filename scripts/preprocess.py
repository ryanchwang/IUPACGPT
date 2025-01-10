import cv2
import numpy as np
import matplotlib.pyplot as plt


def preprocess_image(image_path, output_path):
    # Load the image from the file path
    image = cv2.imread(image_path)

    if image is None:
        raise ValueError("Image not found. Check the path.")
    
    # Resize the image to 500x500 pixels
    image = cv2.resize(image, (500, 500))
    
    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Apply a bilateral filter to reduce noise and keep edges sharp
    #filtered_image = cv2.bilateralFilter(gray_image, d=9, sigmaColor=75, sigmaSpace=75)
    
    # Use Canny edge detector to detect edges in the image
    #edges = cv2.Canny(filtered_image, threshold1=50, threshold2=150)
    
    # Save the final image with edges detected
    cv2.imwrite(output_path, gray_image)

    return output_path
    
    # Optionally display the final image
    '''
    cv2.imshow('Final Processed Image')
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    '''

def harris_method(image_path):
    img = cv2.imread(image_path)
    if img is None:
        raise ValueError("Image not found. Check the path.")

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    corners = cv2.goodFeaturesToTrack(
        gray,
        maxCorners=500,
        qualityLevel=0.001,
        minDistance=20,
        useHarrisDetector=True,
        k=0.04
    )

    if corners is not None:
        corners = corners.astype(np.int64)
        for c in corners:
            x, y = c.ravel()
            img = cv2.circle(img, center=(x, y), radius=5, color=(0, 255, 0), thickness=-1)

    # Display the image (optional)
    cv2.imshow("Detected Corners", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Return the array of corners or an empty list if no corners found
    return corners if corners is not None else []



