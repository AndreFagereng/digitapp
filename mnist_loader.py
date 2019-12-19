import tensorflow_datasets as tfds
import tensorflow as tf


def load_mnist_digits():
	return tf.keras.datasets.mnist.load_data(path='mnist.npz')



# Downloads if MNIST is not downloaded, else loads and returns the data
"""def dl_load_mnist(data_dir, download=True):
	SPLIT_WEIGHTS = (8, 2)
	splits = tfds.Split.TRAIN.subsplit(weighted=SPLIT_WEIGHTS)
	(train, test), info = tfds.load(
		with_info=True, 
		data_dir=data_dir, 
		name="mnist", 
		download=download, 
		split=splits)
	#mnist_test = tfds.load(data_dir=data_dir,name="mnist", split="test", download=download)

	return (train, test), info
"""
#train, test = dl_load_mnist(split='all', data_dir='data', download=True)

