import tensorflow_datasets as tfds
import tensorflow as tf

tf.compat.v1.enable_eager_execution()

# Downloads if MNIST is not downloaded, else loads and returns the data

def dl_load_mnist(split, data_dir, download=True):

	mnist_train = tfds.load(data_dir=data_dir, name="mnist", split="train", download=download)
	mnist_test = tfds.load(data_dir=data_dir,name="mnist", split="test", download=download)
	assert isinstance(mnist_train, tf.data.Dataset)
	assert isinstance(mnist_test, tf.data.Dataset)
	
	return mnist_train, mnist_test

#train, test = dl_load_mnist(split='all', data_dir='data', download=True)

