from app import app

@app.route("/")
def index():
	return "Hello from views"

@app.route("/about")
def about():
	return "About"