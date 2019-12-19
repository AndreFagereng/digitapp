from app import app
import os
from models import CNN_model, DNN_model
from utils import png_to_array
import numpy as np

data_path = 'data'
uploaded  = '/uploaded_img'
mnist_dta = '/mnist'


if __name__ == "__main__":

	# Creates paths to data resources and uploaded digits
	path_data = os.path.join(data_path, uploaded)

	if not (os.path.exists(data_path)):
		os.mkdir(data_path)
		os.mkdir(path_data)


	# Runs the flask app
	app.run(debug=True)