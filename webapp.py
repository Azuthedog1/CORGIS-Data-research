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

@app.route("/stats")
def render_respose1():
	with open('earthquakes.json') as earthquake_data:
		locations = json.load(earthquake_data)
	return render_template('stats.html', response = get_state_options(locations))

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

def get_state_options(locations):
	get_state_options = []
	for s in locations:
		if not(s['location']['name']) in get_state_options:
			get_state_options.append(s['location']['name'])
	get_state_options.sort()
	y = ''
	for x in get_state_options:
		y = y + Markup("<option value=\"" + x + "\">" + x + "</option>")
	return y

@app.route("/response")
def render_response():
	with open('earthquakes.json') as earthquake_data:
		locations = json.load(earthquake_data)
	place = request.args['PlaceSelected']
	fact = place
	fact1 = 0
	for data in locations:
		if place == data["location"]["name"]:
			fact1 = fact1 + 1
	return render_template('response.html', response2 = fact, response3 = fact1)

if __name__=="__main__":
    app.run(debug=True, port=54321)
