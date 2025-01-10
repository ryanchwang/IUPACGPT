import os
from scripts.edge_to_ethane import edge_to_ethane_name
from scripts.preprocess import harris_method, preprocess_image
import matplotlib.pyplot as plt
import cv2
import numpy as np

def main():
    print("Starting program...")
    input_image_path = "data/molecule_2.png"
    output_image_path = "data/processed_image.png"

    # Step 1: Process the image
    print("Processing image...")
    edge_image = preprocess_image(input_image_path, output_image_path)
    print("Image processing complete.")

    # Step 2: Count edges
    print("Counting edges...")
    point_count = harris_method(output_image_path)
    print(f"Number of points detected: {point_count}")

    # Step 3: Convert edge count to name
    print("Converting edge count to compound name...")
    compound_name = edge_to_ethane_name(len(point_count))
    print(f"Compound name: {compound_name}")

    # Step 4: Display images
    

if __name__ == "__main__":
    main()






