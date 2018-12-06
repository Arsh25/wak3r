#!/usr/bin/env python3.5

from flask import Flask, render_template, redirect, url_for, request, jsonify, make_response
from flask_pymongo import PyMongo
from api import format_data, get_database
import json


app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/wakeme" #python3
#app.config['MONGO_DBNAME'] = 'wakeme' #python2
mongo = PyMongo(app)


# where the magic happens
@app.route('/', methods = ['GET', 'POST'])
def index():
	if request.method == 'POST':
		if request.data:
			seek = json.loads(request.data)
			if seek['purpose'] == 'del':
				del_db({"days" : seek['data']['days'], "hrs" : seek['data']['hrs'], "mins" : seek['data']['mins']})
				print(get_db())
		else:
			days = request.form.getlist('day')
			hrs = request.form['hours']
			mins = request.form['minutes']

			if mins == "0" or mins == "5":
				mins = "0" + mins

			set_db(days, hrs, mins)

		return redirect(url_for('index'))
	elif request.method == 'GET':
		return render_template('index.html', settings = get_db())


# add a setting to the db
def set_db(days, hrs, mins):
	mongo.db.current.insert({'days' : days, 'hrs' : hrs, 'mins' : mins})


# get every setting we've stored
def get_db():
	current = mongo.db.current.find({})
	cur_list = []

	for c in current:
		cur_list.append( {'days' : c['days'], 'hrs' : c['hrs'], 'mins' : c['mins']} )

	return cur_list


# delete an item from the database
def del_db(to_rm):
	mongo.db.current.remove({"days" : to_rm['days'], "hrs" : to_rm['hrs'], "mins" : to_rm['mins']})


# secret page, shh...
@app.route('/get_times', methods = ['GET'])
def get_times():
	data = get_db()

	clock = []

	for i in range(len(data)):
		days = data[i]['days']
		time = data[i]['hrs'] + ":" + data[i]['mins']
		clock.append({"days" : days, "time" : time})

	return jsonify(clock)
	#return get_database(db_file='db.json')


if __name__ == '__main__':
	app.run()