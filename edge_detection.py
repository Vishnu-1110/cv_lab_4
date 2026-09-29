import cv2
import numpy as np
import matplotlib.pyplot as plt


def show_comparison(original, sobel, prewitt, canny):
    plt.figure(figsize=(12, 10))

    plt.subplot(2, 2, 1)
    plt.imshow(original, cmap="gray")
    plt.title("Original grayscale image")
    plt.axis("off")

    plt.subplot(2, 2, 2)
    plt.imshow(sobel, cmap="gray")
    plt.title("Sobel edge detection")
    plt.axis("off")

    plt.subplot(2, 2, 3)
    plt.imshow(prewitt, cmap="gray")
    plt.title("Prewitt edge detection")
    plt.axis("off")

    plt.subplot(2, 2, 4)
    plt.imshow(canny, cmap="gray")
    plt.title("Canny edge detection")
    plt.axis("off")

    plt.tight_layout()
    plt.show()


# Read the image in grayscale
img = cv2.imread("images2.jpg", 0)

if img is None:
    print("Error: Image not found")
else:
    # Sobel operator: gradient in X and Y directions
    sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
    sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)

    # Combine Sobel gradients
    sobel_combined = cv2.magnitude(sobelx, sobely)

    # Prewitt operator
    kernelx = np.array([[1, 1, 1],
                        [0, 0, 0],
                        [-1, -1, -1]])

    kernely = np.array([[-1, 0, 1],
                        [-1, 0, 1],
                        [-1, 0, 1]])

    prewittx = cv2.filter2D(img, -1, kernelx)
    prewitty = cv2.filter2D(img, -1, kernely)

    # Combine Prewitt gradients
    prewitt_combined = cv2.addWeighted(
        cv2.convertScaleAbs(prewittx), 0.5,
        cv2.convertScaleAbs(prewitty), 0.5,
        0
    )

    # Canny edge detection
    canny = cv2.Canny(img, 100, 200)

    # Display results
    show_comparison(img, sobel_combined, prewitt_combined, canny)
