Object Detection is a task that requires segmenting and detecting objects from the input image. The common step used are:

    Step1: Dataset Preparation
Obtain the image you want to perform object recognition on. This could be an image from a camera feed, a file on disk, or any other source.
    
    Step2: Choosing a Pre-trained model
Download or load a pre-trained model. There are many deep learning frameworks for object recognition like CNN, R-CNN, Faster R-CNN, YOLO and SSD.
    
    Step3: Train the model
Divide the dataset into Training and Testing datasets. Usually the division is made by 80-20 rule. The training set is used to train the model on.

    Step4: Evaluate the model
Training the model will be used to evaluate the result. The model will output predictions such as bounding boxes, class labels, and confidence scores for detected objects.
    
    Step5: Testing the model
Use the same model on the testing dataset.
    
    Step6: Post-processing
Post-processing involves interpreting the model's predictions. Common post-processing steps include filtering out low-confidence predictions, applying non-maximum suppression to remove redundant bounding boxes
    
    Step7: Visualization
Display the original image with annotated bounding boxes and class labels representing the detected objects.

Here, we have used YOLO, a deep learning framework for object recognition. YOLO is abbreviated as "You Only Look Once." YOLO is a family of real time object detection methods used in computer vision. It uses a single forward pass using a neural network. There are many versions of YOLO i.e. YOLOv4, YOLOv5 YOLOv7, YOLOv8, etc. In the current model implemented above, I have used YOLOv3. It clearly detects the objects in the input image, if that object is already trained in "coco.names ". It can also be used to train user defined objects.

**Python Code Implementation:**

Import Numpy : [pip install numpy]

Load Yolo weights : [yolo_weights](https://github.com/patrick013/Object-Detection---Yolov3/blob/master/model/yolov3.weights)
