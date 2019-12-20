from app import app
from flask import render_template, request, redirect, jsonify
import os
import base64
import time
from utils import png_to_array
from models import CNN_model, DNN_model
import numpy as np
import json


@app.route("/", methods=['GET'])
def index():
	return render_template("index.html")

@app.route('/upload-image', methods=['GET','POST'])
def upload_image():

	if request.method == 'POST':
		img_b64 = request.values['imageBase64'].split(',')
		algorithm = request.values['algorithm']
		print(algorithm)
		img_decoded = base64.b64decode(img_b64[1])

		image_path = save_image(img_decoded)
		argmax, confidense = predict_image(image_path, algorithm)
		

		return jsonify({
			'prediction' : str(argmax),
			'confidense' : str(confidense)})

	return render_template("index.html")

# Saves image to file
def save_image(image):
	# Relative path to uploaded images
	path = 'data/uploaded_img/' 
	
	# Converts time to unique filenames
	filename = str(time.strftime('%Y%m%d-%H%M%S'))
	with open(path + filename + '.png', 'wb') as file:
		file.write(image)
	return str(os.path.join(path, filename))

def predict_image(image_path, model):

	image = png_to_array(image_path + '.png')

	if model == 'CNN':

		cnn = CNN_model()
		cnn.load_weights('./checkpoints/checkpoint_1')

		prediction = cnn.predict(image)
		argmax = np.argmax(prediction)


		return argmax, np.round((prediction[0][argmax]*100), 2)

	elif model == 'DNN':

		dnn = DNN_model()
		dnn.load_weights('./checkpoints/dnn/checkpoints_1')

		prediction = dnn.predict(image)
		argmax     = np.argmax(prediction)
		print('DNN WORKING..')

		return argmax, np.round((prediction[0][argmax]*100), 2)

	return 1

