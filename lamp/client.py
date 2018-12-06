#!/usr/bin/env python3.5

import serial
import requests
from datetime import datetime,timedelta
from datetime import date
import time

class LampClient():
	
	def __init__(self,serial_port,baud_rate,server_url,time_format='%w:%H:%M'):
		self.serial_port = serial_port
		self.server_url = server_url
		self.baud_rate = baud_rate
		self.time_format = time_format
	
	def serial_open(self):
		port = serial.Serial(self.serial_port,self.baud_rate)
		port.open()
		return port
	
	def get_latest_data(self):
		self.today = datetime.now()
		req = requests.get(self.server_url+'/get_times')
		self.latest_data = req.json()
		return self.latest_data
	
	def convert_to_datetime(self):
		self.times = []
		for key in self.latest_data.keys():
			if key != 'last_modified':
				for day in range(7):
					if self.latest_data[key][day] == 1:
						if day == 0:
							correct_day = 6
						else:
							correct_day = day-1
						time_string = str(correct_day)+':'+key
						print(time_string)
						self.times.append(time_string)

if __name__ == '__main__':
	my_lamp = LampClient('fake_serial',9600,'http://localhost:5000')
	print(my_lamp.get_latest_data())
	my_lamp.convert_to_datetime()
	# print(my_lamp.times)
	print(my_lamp.today.weekday())
	for time in my_lamp.times:
		print(time)	