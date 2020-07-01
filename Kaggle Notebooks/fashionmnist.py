# This Python 3 environment comes with many helpful analytics libraries installed
# It is defined by the kaggle/python Docker image: https://github.com/kaggle/docker-python
# For example, here's several helpful packages to load

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

# Input data files are available in the read-only "../input/" directory
# For example, running this (by clicking run or pressing Shift+Enter) will list all files under the input directory

import os
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

# You can write up to 5GB to the current directory (/kaggle/working/) that gets preserved as output when you create a version using "Save & Run All" 
# You can also write temporary files to /kaggle/temp/, but they won't be saved outside of the current session

import tensorflow as tf

'''Loding the fashion MNIST data directly from the tf.keras API'''
mnist = tf.keras.datasets.fashion_mnist

(training_images,training_labels),(test_images,test_labels) = mnist.load_data()

'''Viewing the values that are stord in the dataset using numpy and matplotlib library'''
import numpy as np
import matplotlib.pyplot as plt

plt.imshow(training_images[0])
#print(training_images[0])
#print(test_images[0])

'''The image values lies between 0 and 255. So first of all we have to convert these values from 0-255 to 0-1.'''
training_images = training_images/255
test_images = test_images/255
#print(training_images[0])

'''Now lets design a model'''
model = tf.keras.Sequential([tf.keras.layers.Flatten(),
                            tf.keras.layers.Dense(128,activation=tf.nn.relu),
                            tf.keras.layers.Dense(10,activation=tf.nn.softmax)])

'''Sequential: That defines a SEQUENCE of layers in the neural network

Flatten: Remember earlier where our images were a square, when you printed them out? Flatten just takes that square and turns it into a 1 dimensional set.

Dense: Adds a layer of neurons

Each layer of neurons need an activation function to tell them what to do. There's lots of options, but just use these for now.

Relu effectively means "If X>0 return X, else return 0" -- so what it does it it only passes values 0 or greater to the next layer in the network.

Softmax takes a set of values, and effectively picks the biggest one, so, for example, if the output of the last layer looks like [0.1, 0.1, 0.05, 0.1, 9.5, 0.1, 0.05, 0.05, 0.05], it saves you from fishing through it looking for the biggest value, and turns it into [0,0,0,0,1,0,0,0,0] -- The goal is to save a lot of coding!'''


'''Now compiling and fitting the model'''
model.compile(optimizer = tf.optimizers.Adam(),
              loss = 'sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(training_images, training_labels, epochs=5)

'''Evaluating our model'''
model.evaluate(test_images, test_labels)