import cv2
import numpy as np
import matplotlib.pyplot as plt

def sobel_edge_detection(image_path):
    # Load image in grayscale
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    if image is None:
        print("Error: Image not found.")
        return

    # Apply Sobel edge detection
    sobel_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)
    sobel_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)
    sobel_combined = cv2.magnitude(sobel_x, sobel_y)

    # Display the result
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 3, 1), plt.title('Original'), plt.imshow(image, cmap='gray')
    plt.subplot(1, 3, 2), plt.title('Sobel X'), plt.imshow(np.abs(sobel_x), cmap='gray')
    plt.subplot(1, 3, 3), plt.title('Sobel Y'), plt.imshow(np.abs(sobel_y), cmap='gray')
    plt.show()

def canny_edge_detection(image_path):
    # Load image in grayscale
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    if image is None:
        print("Error: Image not found.")
        return

    # Apply Canny edge detection
    edges = cv2.Canny(image, 100, 200)

    # Display the result
    plt.title('Canny Edge Detection'), plt.imshow(edges, cmap='gray')
    plt.show()

image_path = 'Image Handling/0.jpg'
image_path='images/04 Horse.jpg'

# image_path = input("Enter image path: ")
canny_edge_detection(image_path)




sobel_edge_detection(image_path)



