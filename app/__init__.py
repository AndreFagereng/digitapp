from flask import Flask

app = Flask(__name__)

UPLOAD_FOLDER = 'C:/Users/Jegern/Desktop/github/digitapp/data/uploaded_img'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

from app import views
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['IMAGE_UPLOADS'] = UPLOAD_FOLDER