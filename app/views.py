from app import app
from flask import render_template, request, redirect
import os
import base64
import time


@app.route("/", methods=['GET'])
def index():
	return render_template("index.html")

@app.route('/upload-image', methods=['GET','POST'])
def upload_image():

	if request.method == 'POST':
		img_b64 = request.values['imageBase64'].split(',')
		algorithm = request.values['algorithm']

		img_decoded = base64.b64decode(img_b64[1])
		try:
			save_image(img_decoded)
		except:
			print('An error occured while saving image.')

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




