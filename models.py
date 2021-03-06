import tensorflow as tf
from tensorflow.keras import datasets, layers, models
from utils import load_mnist_digits
import numpy as np
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from config import _config

class DNN_model(tf.keras.Model):
	def __init__(self):
		super(DNN_model, self).__init__()
		self.flatt  = tf.keras.layers.Flatten()
		self.dense1 = tf.keras.layers.Dense(512, activation='relu', input_shape=(784,))
		self.dense2 = tf.keras.layers.Dense(256, activation='relu')
		self.dense3 = tf.keras.layers.Dense(128, activation='relu')
		self.dense4 = tf.keras.layers.Dense(64, activation='relu')
		self.softmax = tf.keras.layers.Dense(10, activation='softmax')

	def call(self, inputs):
		x = self.flatt(inputs)
		x = self.dense1(x)
		x = self.dense2(x)
		x = self.dense3(x)
		x = self.dense4(x)
		return self.softmax(x)


class CNN_model(tf.keras.Model):

	def __init__(self):
		super(CNN_model, self).__init__()
		self.conv1 = tf.keras.layers.Conv2D(32, (5, 5), activation='relu', input_shape=(28, 28, 1))
		self.max1  = tf.keras.layers.MaxPooling2D((2,2))
		self.conv2 = tf.keras.layers.Conv2D(64, (3,3), activation='relu')
		self.max2  = tf.keras.layers.MaxPooling2D((2,2))
		self.conv3 = tf.keras.layers.Conv2D(24, (3,3), activation='relu')
		self.flatt = tf.keras.layers.Flatten()
		self.dense1= tf.keras.layers.Dense(100, activation='relu')
		self.softmax= tf.keras.layers.Dense(10, activation='softmax')

	def call(self, inputs):
		x = self.conv1(inputs)
		x = self.max1(x)
		x = self.conv2(x)
		x = self.max2(x)
		x = self.conv3(x)
		x = self.flatt(x)
		x = self.dense1(x)
		
		return self.softmax(x)

def fit_models():


	EPOCHS  = _config['CNN']['EPOCHS']
	BATCH_S = _config['CNN']['BATCH_S'] 
	LEARNING_RATE = _config['CNN']['LEARNING_RATE']
	MOMENTUM	  = _config['CNN']['MOMENTUM']
	
	optimizer_sgd = tf.keras.optimizers.SGD(
		learning_rate=LEARNING_RATE,
		momentum=MOMENTUM)

	optimizer_adam = tf.keras.optimizers.Adam()

	dnn = DNN_model()
	cnn = CNN_model()

	dnn.compile(
		optimizers=optimizer_sgd,
		loss='sparse_categorical_crossentropy',
		metrics=['accuracy'])
	
	cnn.compile(optimizers=optimizer_sgd,
				loss='sparse_categorical_crossentropy',
				metrics=['accuracy'])
	
	# Loading the data and normalizing its values {0-1}
	(X_train, y_train), (X_test, y_test) = load_mnist_digits()
	X_train, X_test = X_train / 255.0, X_test / 255.0

	# Creates a ImageDataGenerator which augments images
	# in parallel while training.
	datagen= ImageDataGenerator(
			rotation_range=20,
			width_shift_range=0.2,
			height_shift_range=0.2,
			horizontal_flip=True
		)


	# Add an axis because fit methods is complaining about dimensions.
	X_train = X_train[..., tf.newaxis]
	X_test = X_test[..., tf.newaxis]

	# Fitting the ImageDataGenerator with the training data
	datagen.fit(X_train)

	print('Training CNN..')
	cnn.fit_generator(datagen.flow(
		X_train,
		y_train, 
		batch_size=BATCH_S),
		epochs=EPOCHS,
		verbose=1,
		shuffle=True,
		validation_data=(X_test, y_test))

	print('Training DNN..')
	dnn.fit_generator(datagen.flow(
		X_train,
		y_train, 
		batch_size=BATCH_S),
		epochs=EPOCHS,
		verbose=1,
		shuffle=True,
		validation_data=(X_test, y_test))

	cnn.save_weights('./checkpoints/checkpoint_1')
	dnn.save_weights('./checkpoints/dnn/checkpoints_1')

#history_cnn = cnn.fit(
#	x=X_train, 
#	y=y_train,
#	epochs=EPOCHS,
#	batch_size=BATCH_S,
#	shuffle=True,
#	validation_data=(X_test, y_test),
#	)
	#history_dnn = dnn.fit(
#	x=X_train, 
#	y=y_train,
#	epochs=EPOCHS,
#	batch_size=BATCH_S,
#	shuffle=True,
#	validation_data=(X_test, y_test),
#	)