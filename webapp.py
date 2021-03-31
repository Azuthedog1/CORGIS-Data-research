from flask import Flask, request, Markup, render_template, flash, Markup
import os
import json

app = Flask(__name__)

@app.route("/")
def render_main():
	with open('earthquakes.json') as earthquake_data:
		locations = json.load(earthquake_data)
	#return render_template('home.html', options = get_location_options(locations))
	return render_template('home.html')

@app.route("/response")
def render_response():
	#with open('earthquakes.json') as earthquake_data:
		#locations = json.load(earthquake_data)
	#location = request.args['LocationSelected']
	fact1 = 0
	#for data in location:
		#if place == data["location"]["name"]:
			#factC = data["Miscellaneous"]["Language Other than English at Home"]
			#factS = data["State"]
	return render_template('response.html', response = fact1)


if __name__=="__main__":
    app.run(debug=True, port=54321)
