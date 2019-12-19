import tensorflow as tf
from PIL import Image
import numpy as np
from keras.preprocessing import image
	

def load_mnist_digits():
	return tf.keras.datasets.mnist.load_data(path='mnist.npz')

def png_to_array(path):

	img_width, img_height = 28, 28
	img = image.load_img(path, grayscale=True, target_size = (img_width, img_height))
	img = image.img_to_array(img)
	img = np.expand_dims(img, axis = 0)	
	img = img / 256

	return img
