from app import app
from flask import render_template, request, redirect
import os
import base64
import time
from utils import png_to_array
from models import CNN_model
import numpy as np


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
		prediction = predict_image(image_path, algorithm)

		return render_template("index.html")

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
		print('Prediction: ',argmax)
		print(prediction)
		return np.argmax(prediction)

	elif model == 'DNN':
		pass

	return 1

