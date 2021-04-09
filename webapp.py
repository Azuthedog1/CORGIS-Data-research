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

@app.route("/graph")
def render_respose():
	with open('earthquakes.json') as earthquake_data:
		file = json.load(earthquake_data)
	earth = {}
	for x in range(32):
		earth[x] = 0
	return render_template('graph.html', dataPoints=total_daily_earthquakes(file))

def total_daily_earthquakes(file):
	days = {}
	earth = {}
	for x in range(1, 32):
		earth[x] = 0
	for d in file:
		day = d["time"]["day"]
		for y in earth.keys():
			if day == y:
				num = earth.get(y)
				earth[y] = num + 1
	#number_of_earthquakes = []
	#for w in earth:
		#if w < 29 and w > 0:
		#number_of_earthquakes.append(earth.get(w))
	code = "["
	for year, gross in earth.items():
		code = code + Markup("{ x: '" + str(year) + "', y: " + str(earth.get(year)) + " },")
	code = code[:-1] #remove the last comma
	code = code + "]"
	return code




if __name__=="__main__":
    app.run(debug=True, port=54321)
