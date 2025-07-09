
# Advanced Automatic License Plate Recognition (ALPR) Using Deep Learning

This repository presents our final project on developing a deep learning-based system for Automatic License Plate Recognition (ALPR). It improves upon a traditional KNN-based system by replacing the character recognition module with a deep learning model (EasyOCR), resulting in a more robust and accurate pipeline.

## Project Overview

Automatic License Plate Recognition (ALPR) is a computer vision task that identifies and extracts text from vehicle license plates. It has a wide range of real-world applications including:

- Traffic enforcement  
- Toll collection  
- Parking and access control systems

This project aims to build a real-time and accurate ALPR system using deep learning techniques.

## Midterm Recap

In the midterm, a basic ALPR pipeline was implemented using K-Nearest Neighbors (KNN) for character recognition. The pipeline included:

- Image preprocessing  
- License plate detection using contours  
- KNN-based classification for character recognition

Limitations of the midterm system:

- Sensitive to noise, lighting conditions, and skewed plates  
- Inconsistent accuracy on real-world images

## Final Project Objectives

- Replace KNN with a deep learning model for improved character recognition  
- Integrate all steps into a unified and automated ALPR pipeline  
- Improve accuracy and robustness in diverse real-world scenarios

## System Architecture

The full pipeline includes the following stages:

1. Preprocessing  
2. License Plate Detection  
3. Character Recognition using EasyOCR  
4. Visualization and Output

## Dataset Description

- Sourced from Google Images  
- Includes diverse license plates under various lighting and quality conditions  
- Contains both clean and noisy examples to test system robustness

## Preprocessing Pipeline

Implemented in Preprocess.py, this stage prepares the image for plate detection:

- HSV color conversion  
- Contrast enhancement  
- Gaussian blur  
- Adaptive thresholding

## License Plate Detection

Implemented in DetectPlates.py:

- Contour-based filtering  
- Aspect ratio and size constraints used to localize license plates  
- Returns cropped plate regions along with bounding box coordinates

## Character Recognition

Implemented in DetectChars.py:

- Utilizes EasyOCR, a deep learning-based OCR engine  
- Robust to different fonts, lighting, and distortions  
- Replaces the KNN model from the midterm with a significantly more accurate approach

## Integrated Workflow

All components are integrated in Main.py:

- Loads input image  
- Runs plate detection and text extraction  
- Annotates and displays final results

## Challenges Faced

- Variability in license plate formats  
- Low image quality in some real-world examples  
- Difficulties with skewed or partially obscured plates  
- Fine-tuning detection parameters for generalization

## Conclusion

- Successfully built a full ALPR system with improved recognition accuracy  
- Replaced traditional KNN with a deep learning-based OCR model  
- System performs reliably across diverse real-world plate images

## Future Work

- Replace EasyOCR with a custom-trained CRNN model for even higher accuracy  
- Add video stream processing support  
- Implement skew correction and real-time deployment  
- Improve plate detection using YOLO or other object detection models

## References

- OpenCV  
- EasyOCR  
- CRNN Research Paper  
- Python Documentation  
- GitHub resources and tutorials

## How to Run

1. Install dependencies from requirements.txt  
2. Place input images in the input/ directory  
3. Run the pipeline using:

```bash
python Main.py
```
