# Face Recognition System README

This repository contains code for a simple face recognition system built using Python and OpenCV. The system captures faces from a webcam, trains a recognition model, and then detects and recognizes faces in real-time. Below is a guide on how to use and understand the code in this repository.

## Prerequisites

1. **Python**: Make sure you have Python installed on your system. You can download it from the official [Python website](https://www.python.org/downloads/).

2. **OpenCV**: Install the OpenCV library using the following command:
   ```
   pip install opencv-python
   ```

## Code Structure

The repository contains three Python scripts: `face_detector.py`, `training.py`, and `face_recognition.py`. Here's a brief overview of each script's functionality:

### `face_detector.py`

This script captures images from the webcam and saves them to build a dataset for training the recognition model. It detects faces using the Haar Cascade classifier and saves grayscale face images in the `dataset` directory.

### `face_train.py`

This script reads the captured face images from the `dataset` directory, processes them, and trains a face recognition model using the LBPH (Local Binary Pattern Histogram) algorithm. The trained model is then saved as `trainer.yml` in the `trainer` directory.

### `face_recognition.py`
You can see the face_recognition.py file in the repository.

This script uses the trained recognition model to detect and recognize faces in real-time using the webcam feed. Detected faces are framed with rectangles, and recognized names are displayed alongside confidence percentages.

## Usage

1. **Capturing Faces for Training**:

   Run the `face_detector.py` script to capture images for training. The script will prompt you to enter a user ID. Position your face in front of the webcam, and the script will automatically save face images with the specified user ID in the `dataset` directory. Press the `ESC` key to exit the image capturing process. The process will stop after collecting 30 images or when you manually exit.

2. **Training the Recognition Model**:

   After capturing images, run the `training.py` script to process and train the recognition model. The script will read the face images from the `dataset` directory, detect faces, and build a recognition model using the LBPH algorithm. The trained model will be saved as `trainer.yml` in the `trainer` directory.

3. **Real-Time Face Recognition**:

   Run the `face_recognition.py` script to perform real-time face recognition using the trained model. The script will open a webcam feed and detect faces. Recognized faces will be labeled with names, and confidence percentages will be displayed. Press the `ESC` key to exit the real-time recognition.

## Notes

- The accuracy of the face recognition system might vary based on factors like lighting conditions, face angles, and the quality of captured images.
- The `haarcascade_frontalface_default.xml` file is required for face detection. Make sure it's available in the same directory as the scripts.

## Acknowledgments

The code in this repository is based on OpenCV's face detection and recognition capabilities. The Haar Cascade classifier and LBPH algorithm are used for face detection and recognition, respectively.

Feel free to explore, modify, and improve this code for your own projects!

For any questions or issues, please don't hesitate to reach out by opening an issue in this repository.
