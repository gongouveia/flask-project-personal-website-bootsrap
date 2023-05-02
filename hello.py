from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def index():
	#return "hello world!!!"

	first_name = "Paiva"	
	favorite_job = ["bank", "SW", "Embedd"]
	return render_template('index.html', 
				           first_name = first_name,
				           favorite_job = favorite_job)


@app.route('/about')
def about():
	return render_template('about.html')