## Using DNN for Classification in MNIST Dataset

The MNIST dataset is a widely-used benchmark dataset in the field of machine learning and computer vision. It consists of 28x28 pixel grayscale images of handwritten digits (0-9) along with their corresponding labels. The task is to classify these images into their respective digit classes.

### Deep Neural Networks (DNNs) for Classification

Deep Neural Networks (DNNs) have shown remarkable performance in image classification tasks, including the MNIST dataset. DNNs are capable of automatically learning hierarchical features from raw input data, making them well-suited for tasks involving image data.

### Steps Involved in Using DNN for Classification in MNIST Dataset

1. **Data Preparation**: Load the MNIST dataset, which typically comes pre-packaged with popular machine learning libraries like TensorFlow or PyTorch. Preprocess the images by normalizing pixel values and splitting the dataset into training and testing sets.

2. **Model Architecture**: Define a DNN architecture suitable for image classification. This may include convolutional layers followed by fully connected layers. Experiment with different architectures and hyperparameters to find the best model for the task.

3. **Training**: Train the DNN on the training set using techniques such as stochastic gradient descent (SGD) or Adam optimization. Monitor the training process by tracking metrics such as loss and accuracy.

4. **Evaluation**: Evaluate the trained model on the test set to assess its performance. Calculate metrics such as accuracy, precision, recall, and F1-score to measure the model's effectiveness in classifying digits.

5. **Inference**: Once trained, the DNN can be used to classify new, unseen images of handwritten digits with high accuracy.

### Required Dataset ###
1. [MNIST Dataset](https://drive.google.com/drive/folders/1tcy9DMaT1kyWQUz0XK2BdWAvQZJeqGgM)

**Python Code Implementation:**

Import OneHotEncoder : [pip install sklearn]

Import Tensorflow : [pip install tensorflow]

Import Numpy : [pip install numpy]

Import Keras : [pip install keras]

For Dataset : [MNIST Datatset](https://drive.google.com/drive/folders/1tcy9DMaT1kyWQUz0XK2BdWAvQZJeqGgM)
