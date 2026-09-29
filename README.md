# Computer Vision Lab 4 — Edge Detection

This project demonstrates **edge detection techniques in Python using OpenCV, NumPy, and Matplotlib**.

The program reads a grayscale image and compares three commonly used edge detection methods:

- **Sobel Edge Detection**
- **Prewitt Edge Detection**
- **Canny Edge Detection**

## 📌 Objective

To understand and implement different edge detection operators and visually compare the edges detected in a grayscale image.

## 🛠️ Technologies Used

- Python 3
- OpenCV
- NumPy
- Matplotlib

## 📂 Project Structure

```text
cv_lab_4/
├── edge_detection.py
├── requirements.txt
├── images2.jpg
├── output/
│   └── edge_detection_output.png
└── README.md
```

## ⚙️ Installation

Install the required Python libraries:

```bash
pip install -r requirements.txt
```

## ▶️ How to Run

1. Place the input image as `images2.jpg` in the project folder.
2. Run the Python program:

```bash
python edge_detection.py
```

3. A Matplotlib window will display the original grayscale image along with the Sobel, Prewitt, and Canny edge-detection results.

> **Note:** The original lab code used a Google Colab path. This repository version uses the simpler local path `images2.jpg`, so it can be run directly after placing the image in the project folder.

## 🔍 Methods Used

### 1. Sobel Edge Detection

The Sobel operator calculates image intensity gradients in the horizontal and vertical directions. The two gradients are combined to highlight strong edges.

### 2. Prewitt Edge Detection

The Prewitt operator uses two 3×3 convolution kernels to detect horizontal and vertical intensity changes.

### 3. Canny Edge Detection

Canny is a multi-stage edge detector that uses gradient calculation, non-maximum suppression, double thresholding, and edge tracking to produce thin edges.

## 📊 Output

The program produces a comparison containing:

1. Original grayscale image
2. Sobel edge detection
3. Prewitt edge detection
4. Canny edge detection

### Output Image

![Edge Detection Output](output/edge_detection_output.png)

## 🧪 Result

The output shows how the three edge detection techniques identify boundaries and intensity changes in the image. Sobel and Prewitt use gradient-based convolution, while Canny produces a thin binary-style edge map after additional processing.

## 👨‍💻 Author

**Vishnu Vardhan**

GitHub: [Vishnu-1110](https://github.com/Vishnu-1110)
