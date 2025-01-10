import os
from scripts.edge_to_ethane import edge_to_ethane_name
from scripts.preprocess import preprocess_image, count_edges
import matplotlib.pyplot as plt
import cv2

def main():
    input_image_path = "data/molecule_0.png"
    output_image_path = "data/processed_image.png"


    print("Processing image...")
    preprocess_image(input_image_path, output_image_path)

    edge_image = cv2.imread(output_image_path, cv2.IMREAD_GRAYSCALE)

    # Count edges
    edge_count = count_edges(edge_image)
    print(f"Number of edges detected: {edge_count}")

    #convert to name
    compound_name = edge_to_ethane_name(edge_count)
    print(f"The compound name based on edges is: {compound_name}")

    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.title("Edge Detection")
    plt.imshow(edges, cmap='gray')
    plt.subplot(1, 2, 2)
    plt.title("Original Image")
    plt.imshow(cv2.imread(image_path)[:, :, ::-1])  # Convert BGR to RGB for display
    plt.show()

if __name__ == "__main__":
    main()






