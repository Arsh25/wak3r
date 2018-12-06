#!/usr/bin/env python3.5

import serial
import requests
from datetime import datetime,timedelta
from datetime import date
import time

class LampClient():
	next_turn_on = None
	def __init__(self,serial_port,baud_rate,server_url,time_format='%w:%H:%M'):
		self.serial_port = serial_port
		self.server_url = server_url
		self.baud_rate = baud_rate
		self.time_format = time_format
	
	def serial_open(self):
		port = serial.Serial(self.serial_port,self.baud_rate,timeout=.5)
		try:
			port.open()
		except serial.SerialException:
			port.close()
			port.open()
		self.port = port
		return port
	def serial_close(self):
		self.port.close()
	def serial_write(self,byte):
		return self.port.write(byte)

	def get_latest_data(self):
		self.today = datetime.now()
		req = requests.get(self.server_url+'/get_times')
		self.latest_data = req.json()
		return self.latest_data
	
	def convert_to_datetime(self):
		self.get_latest_data()
		self.times = []
		for alarm in self.latest_data:
			my_time = alarm['time']
			for day in range(7):
				if str(day) in alarm['days']:
					if day == 0:
						correct_day = 6
					else:
						correct_day = day-1
					time_string = str(correct_day)+':'+my_time
					self.times.append(time_string)

	def get_turn_on_times_for_today(self):
		self.convert_to_datetime()
		self.current_time = datetime.now()
		self.today_times = []
		self.turn_on_today = False
		for my_time in self.times:
			my_time = my_time.split(':')
			if int(my_time[0]) == self.current_time.weekday():
				if int(my_time[1]) == self.current_time.hour:
					if int(my_time[2]) > self.current_time.minute:
						turn_on_string = my_time[1]+':'+my_time[2]
						self.today_times.append(datetime.strptime(turn_on_string,'%H:%M'))
						self.turn_on_today = True
				elif int(my_time[1]) > self.current_time.hour:
					turn_on_string = my_time[1]+':'+my_time[2]
					self.today_times.append(datetime.strptime(turn_on_string,'%H:%M'))
					self.turn_on_today = True

	def get_next_turn_on(self):
		self.get_turn_on_times_for_today()
		if len(self.today_times) >0:
			self.next_turn_on = min(self.today_times)
			current_time = datetime.now()
			while True:
				if self.next_turn_on.hour > current_time.hour:
						break
				elif self.next_turn_on.hour == current_time.hour:
					if self.next_turn_on.minute >= current_time.minute:
						break
				else:
					min_index = today_times.index(min(self.today_times))
					self.next_turn_on = min(self.today_times[:min_index],self.today_times[min_index+1:])

if __name__ == '__main__':
	my_lamp = LampClient('/dev/ttyACM0',9600,'http://localhost:5000')	
	my_lamp.get_next_turn_on()
	# print(my_lamp.next_turn_on)
	# serial_port = my_lamp.serial_open()
	# print(serial_port.is_open)
	# print(my_lamp.serial_write(b'1'))
	# time.sleep(5)
	# print(my_lamp.serial_write(b'0'))
	# my_lamp.serial_close()
	# print(serial_port.is_open)
	print(my_lamp.times)
	print(my_lamp.next_turn_on)