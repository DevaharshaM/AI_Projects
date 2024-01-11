Face Detection is a computer vision task that involves identifying and detecting faces from an image or video. There are several steps used for face detection:

    Step1 : Image Preprocessing
The image is preprocessed before extracting the features. These preprocessing steps involves convertion of RGB to Grayscale image, Image sparpening, resizing, etc.
    
    Step2 : Feature Extraction
Here, we are using haar cascade detectors for feature extraction. Haar cascade detectors uses Haar feature which are smaller rectagular filters that can be applied to an image
    
    Step3 : Integral Image
The integral image allows for the rapid calculation of the sum of pixel values within any rectangular region of the image
    
    Step4 : Sliding Window
A Haar cascade detector uses a sliding window approach to scan the image at multiple scales and positions. The window is moved across the image, and at each position, the haar like features are computed within the window
    
    Step5 : Haar Casecade classifier
A haar cascade is a classifier that is trained to distinguish between positive faces and negative faces examples.
    
    Step6 : Cascade of classifiers
The cascade structure allows for a quick rejection of non-faces.
    
    Step7 : Thresholding
The output of the cascade classifier is combined to make a final decision about wheather a face is present in a given image.


Here, I have used OpenCV libaray, which includes funtions which helps in importing image, resizing image, visualize image, convertion of image, etc. For detection, I have used Haarcascade classifier, developed by Viola and Jones, which contains a predefined dataset of features of positive faces and negative faces. Rectangle is used to represent the detected image.


**Python Code Implementation:**

Import OpenCV librabry : [pip install opencv-python]

Load Haar Cascade classifier : [HaarCascade_git](https://github.com/opencv/opencv/tree/master/data/haarcascades)