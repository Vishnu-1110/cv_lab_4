# Computer Vision Lab 4 — Edge Detection

This project implements and compares three edge detection techniques on a grayscale image using Python, OpenCV, NumPy, and Matplotlib.

## Objective

To detect and visualize image edges using the Sobel operator, Prewitt operator, and Canny edge detector.

## Libraries Used

- OpenCV
- NumPy
- Matplotlib

## Python Code

The complete program is available in [edge_detection.py](edge_detection.py).

## How It Works

1. The input image is read in grayscale.
2. Sobel filters calculate horizontal and vertical gradients.
3. Prewitt kernels are applied to calculate image gradients.
4. Canny edge detection is applied using thresholds 100 and 200.
5. The original image and the three edge-detection results are displayed together.

## Output

### Edge Detection Comparison

![Edge Detection Output](output/edge_detection_output.jpg)

The output contains:
- Original grayscale image
- Sobel edge detection
- Prewitt edge detection
- Canny edge detection

## Project Files

| File | Description |
|---|---|
| [edge_detection.py](edge_detection.py) | Python implementation |
| [requirements.txt](requirements.txt) | Required libraries |
| [output/edge_detection_output.jpg](output/edge_detection_output.jpg) | Output image |
| [README.md](README.md) | Project documentation |

## Run Locally

Install the required packages:

```bash
pip install -r requirements.txt
```

Run the program:

```bash
python edge_detection.py
```

This version uses a normal local image path and does **not** require Google Colab or Google Drive.

## Result

The program successfully demonstrates and compares Sobel, Prewitt, and Canny edge detection on a grayscale image.

## Author

**Vishnu Vardhan**

GitHub: [Vishnu-1110](https://github.com/Vishnu-1110)
