# Load libraries

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
import keras
import tensorflow as tf

df1 = pd.read_csv('mnist_train.csv')
df2 = pd.read_csv('mnist_test.csv')

X_train, y_train = df1.values[:,:-1], df1.values[:,-1:]
X_test, y_test = df2.values[:,:-1], df2.values[:,-1:]

# Encoding the dataset

onehot = OneHotEncoder()
onehot.fit(y_train)
y_train_onehot = onehot.transform(y_train).toarray()
y_test_onehot = onehot.transform(y_test).toarray()

# Visualization of training data

plt.imshow(X_train[0,:].reshape(28,28), cmap=plt.get_cmap('gray'))
print ('Label of this image:', y_train[0,:])
plt.show()
plt.imshow(X_train[1,:].reshape(28,28), cmap=plt.get_cmap('gray'))
print ('Label of this image:', y_train[1,:])
plt.show()
plt.imshow(X_train[50,:].reshape(28,28), cmap=plt.get_cmap('gray'))
print ('Label of this image:', y_train[50,:])
plt.show()

# Model training

model = keras.Sequential()
model.add(keras.layers.Dense(1024, input_shape=(784,)))
model.add(keras.layers.Activation("relu"))
model.add(keras.layers.Dense(512))
model.add(keras.layers.Activation("relu"))
model.add(keras.layers.Dense(64))
model.add(keras.layers.Activation("relu"))
model.add(keras.layers.Dense(10))
model.add(keras.layers.Activation("softmax"))
model.compile(tf.keras.optimizers.SGD(learning_rate = 1e-3), 'categorical_crossentropy', metrics='acc')
model.summary()
model.fit(X_train, y_train_onehot, epochs = 50, batch_size = 1024, verbose = 2, validation_data = (X_test, y_test_onehot))

# Model testing

prediction = model.predict(X_test)
print (model.evaluate(X_test, y_test_onehot))

# Visualization of testing data

plt.imshow(X_test[0,:].reshape(28,28), cmap=plt.get_cmap('gray'))
print ('Prediction of this image:', np.argmax(prediction[0,:]))
plt.show()
plt.imshow(X_test[1,:].reshape(28,28), cmap=plt.get_cmap('gray'))
print ('Prediction of this image:', np.argmax(prediction[1,:]))
plt.show()
plt.imshow(X_test[50,:].reshape(28,28), cmap=plt.get_cmap('gray'))
print ('Prediction of this image:', np.argmax(prediction[50,:]))
plt.show()
