import keras
import tensorflow as tf
from IPython import display
from keras.preprocessing.image import array_to_img
import matplotlib.pyplot as plt
from numpy.random import seed
seed(888)
tf. set_random_seed(404)
from keras.datasets import cifar10
(x_train,y_train),(x_test,y_test)=cifar10.load_data()
print(type(x_train))



