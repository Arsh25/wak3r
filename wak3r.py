#!/usr/bin/env python

from flask import Flask, render_template, redirect, url_for, request, jsonify, make_response
#from flask_pymongo import PyMongo
import json


app = Flask(__name__)
#app.config['MONGO_DBNAME'] = 'temps'
#mongo = PyMongo(app)


@app.route('/', methods = ['GET', 'POST'])
def index():
	if request.method == 'POST':
		days = request.form.getlist('day')

		hrs = request.form['hours']
		mins = request.form['minutes']
		print("data:", days, hrs, mins)

		return render_template('index.html')
	elif request.method == 'GET':
		return render_template('index.html')


if __name__ == '__main__':
	app.run()
