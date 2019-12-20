from app import app
import os
from models import CNN_model, DNN_model
from utils import png_to_array
import numpy as np
from models import fit_models

import argparse

data_path = 'data'
uploaded  = '/uploaded_img'
mnist_dta = '/mnist'

def define_argparser():
	parser = argparse.ArgumentParser(description='Digit recognizer webapp')
	parser.add_argument('--tm', help='Re-train the model', action="store_true")

	return parser

def cl_args(args):
	if args.tm:
		print('|------------------------|')
		print('|---Re-training models---|')
		print('|------------------------|')
		fit_models()
	return

if __name__ == "__main__":

	# Creates paths to data resources and uploaded digits
	path_data = os.path.join(data_path, uploaded)

	if not (os.path.exists(data_path)):
		os.mkdir(data_path)
		os.mkdir(path_data)

	parser = define_argparser()
	args = parser.parse_args()
	
	cl_args(args)

	# Runs the flask app
	app.run(debug=True)
