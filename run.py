from app import app
import os

data_path = 'data'
uploaded  = '/uploaded_img'
mnist_dta = '/mnist'

if __name__ == "__main__":

	# Creates paths to data resources and uploaded digits
	path_data = os.path.join(data_path, uploaded)
	path_mnist = os.path.join(data_path, mnist_dta)

	if not (os.path.exists(data_path)):
		os.mkdir(data_path)
		os.mkdir(path_data)
		os.mkdir(path_mnist)
	if not os.path.exists('test'):
		os.mkdir('test')

	# Runs the flask app
	app.run(debug=True)