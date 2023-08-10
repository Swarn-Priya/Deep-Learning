# -*- coding: utf-8 -*-
"""Fashion MNIST -  MLP.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1IWGR2ozemUBvrcyGuqesiZrG9C66sxPE
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

import tensorflow as tf
from tensorflow import keras
print(tf.__version__)

f_mnist = keras.datasets.fashion_mnist

f_mnist

(train_images,train_labels),(test_images,test_labels) =f_mnist.load_data()

print(train_images.shape,train_labels.shape)
print(test_images.shape,test_labels.shape)

class_name = ['T-shirt/top', 'Trouser' , 'Pullover','Dress','Coat','Sandal',
              'Shirt','Sneaker','Bag','Ankle boot']

class_name

"""**VIsualization the image**"""

plt.figure()
plt.imshow(train_images[1721])
plt.colorbar()
plt.grid('False')
plt.show()

plt.figure()
plt.imshow(train_images[2117])
plt.colorbar()
plt.show()

"""## **MANDATROY STEP = FEATURE SCALING**

MIN MAX APPROACH **bold text**
"""

train_images = train_images/255.0
test_images = test_images/255.0

plt.figure()
plt.imshow(train_images[2028])
plt.colorbar()
plt.show()

"""After the standarddization, the range comes from 0 to 1....
it was ranging from 0 to 255....so it got changed after standarddization.
"""

plt.figure(figsize = (15,12))

for i in range(25):
  plt.subplot(5,5,i+1)
  plt.xticks([])
  plt.yticks([])
  plt.grid(False)
  plt.imshow(train_images[i],cmap = plt.cm.binary) #cm.binary --- ony two colors will come 0 and 1
  plt.xlabel(class_name[train_labels[i]])

"""DEEP NEURAL NETWORK - Multilayer Perceptron"""

tf.random.set_seed(101) #like random_state
tf.keras.backend.clear_session()

model = None

model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28,28)),
    keras.layers.Dense(128,activation='relu'),
    keras.layers.Dense(10,activation='softmax')
])

"""**HYPARAMETER TUNING.**
1. How many Neurons to be given
2. How many layers to be given
3. how many epochs
4. Which activation function to use
5. which optimization tp be used.
6. WHat should be the learnign rate
"""

model.summary()

from keras.utils import plot_model
plot_model(model,'model.png',show_shapes=True)

model.compile(optimizer='adam',loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics = ['accuracy'])

#TENSORBOARD

import os
import datetime
logdir =os.path.join('logs',datetime.datetime.now().strftime('%Y%m%d-%H%M%S'))
print(logdir)

# Commented out IPython magic to ensure Python compatibility.
# %load_ext tensorboard
# %tensorboard --logdir $logdir

tensorboard_callback = keras.callbacks.TensorBoard(logdir, histogram_freq=1)

model.fit(train_images,train_labels,validation_data=(test_images,test_labels),
          epochs=20,batch_size=64,callbacks=[tensorboard_callback])

DONE

