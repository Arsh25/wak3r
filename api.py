from flask import jsonify 
from flask.json import dump,load
from datetime import datetime,date

def add_time(db_file,data):
	data['last_modified'] = datetime.now().strftime('%d:%m:%y:%H:%M')
	with open(db_file,'w') as db:
		dump(data,db)
def format_days(days_list):
	formatted_data = []
	for day in range(7):
		if day in days_list:
			formatted_data.append(1)
		else:
			formatted_data.append(0)
	return formatted_data

def format_data(days,hour,minute):
	formatted_data = {}
	days = [int(day) for day in days]
	days = format_days(days)
	formatted_data[hour+':'+minute] = days
	add_time('db.json',formatted_data)
	return formatted_data

def get_database(db_file):
	with open(db_file,'r') as db:
		json_data = load(db)
		return jsonify(json_data)
