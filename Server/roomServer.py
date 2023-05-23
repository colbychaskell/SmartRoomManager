import threading
from flask import Flask
from flask import jsonify
from flask import request
from flask import Response

import json
import argparse
import ledManager
import alarmManager

app = Flask('Room Management Server')

@app.route('/led-status', methods=['GET'])
def get_led_status_callback():
	response = jsonify(status=ledManager.led_status)
	response.headers['Access-Control-Allow-Origin'] = '*'

	return response

@app.route('/alarm-on', methods=['GET'])
def set_alarm_on():
	alarmManager.alarm_status = "On"
	alarmManager.detect_motion()
	response = jsonify(status=alarmManager.alarm_status)
	response.headers['Access-Control-Allow-Origin'] = '*'

	return response

@app.route('/alarm-off', methods=['GET'])
def set_alarm_off():
	alarmManager.alarm_status = "Off"
	response = jsonify(status=alarmManager.alarm_status)
	response.headers['Access-Control-Allow-Origin'] = '*'

	return response

@app.route('/alarm-status', methods=['GET'])
def get_alarm_status():
	response = jsonify(status=alarmManager.alarm_status)
	response.headers['Access-Control-Allow-Origin'] = '*'

	return response

@app.route('/occupied', methods=['GET'])
def get_occupied_status():
	response = jsonify(status=alarmManager.occupied)
	response.headers['Access-Control-Allow-Origin'] = '*'

	return response

@app.route('/set-led', methods=['POST'])
def set_led_color():
	color = request.form.get('color')
	
	if color == 'Red':
		ledManager.set_led_red()
	elif color == 'Green':
		ledManager.set_led_green()
	elif color == 'Blue':
		ledManager.set_led_blue()

	response = jsonify(status=ledManager.led_status)
	response.headers['Access-Control-Allow-Origin'] = '*'

	return response

@app.route('/led-off', methods=['GET'])
def get_led_off_callback():
	ledManager.set_led_off()
	response = jsonify(status=ledManager.led_status)
	response.headers['Access-Control-Allow-Origin'] = '*'

	return response



if __name__ == '__main__':
	ledManager = ledManager.ledManager()
	alarmManager = alarmManager.alarmManager()

	app.run(debug=False, host='0.0.0.0', port=5000)