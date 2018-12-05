#!/usr/bin/env python3.5

import serial
import requests

class LampClient():
	def __init__(self,serial_port,baud_rate,server_url):
		self.serial_port = serial_port
		self.server_url = server_url
		self.baud_rate = baud_rate
	def serial_open(self):
		port = serial.Serial(self.serial_port,self.baud_rate)
		port.open()
		return port
	def get_latest_data(self):
		req = requests.get(self.server_url+'/get_times')
		return req.json()

if __name__ == '__main__':
	my_lamp = LampClient('fake_serial',9600,'http://localhost:5000')
	print(my_lamp.get_latest_data())	