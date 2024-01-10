# -*- coding: utf-8 -*-
"""Git_facedetection.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_T8Bmf8zoJzcmcW25YsgRO5gkv_SdFFB
"""

# importing library

import cv2
from google.colab.patches import cv2_imshow

# load the haar cascade classifier
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Read an input image
img = cv2.imread('facedetect.jpg')

# resizing the image
img_resize = cv2.resize(img, (720,480))

# Convert it into a grayscale image
gray = cv2.cvtColor(img_resize, cv2.COLOR_BGR2GRAY)

# Detect faces
faces = face_cascade.detectMultiScale(gray, 1.1, 5)

# Display the detecition results
for (x, y, w, h) in faces:
    cv2.rectangle(img_resize, (x, y), (x+w, y+h), (240, 255, 128), 1)

cv2_imshow(img_resize)