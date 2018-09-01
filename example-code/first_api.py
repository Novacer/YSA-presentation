# Flask is used to make our API 
from flask import Flask
from flask import jsonify
from flask import request

# requests is used to call OTHER people's APIs
import requests

# Machine Learning model that we just made
from .machine_learning.titanic import guess_if_survived



def say_hello(name):
	return "Hello, " + name

	

def get_weather(city):
	weather = requests.get("http://api.openweathermap.org/data/2.5/weather?q=%s&APPID=API_KEY_HERE" % city)
	
	weather_data = weather.json()  # can now access the data
	print(weather_data)
	
	weather_description = weather_data['weather'][0]['description']
	
	response = {'the_weather' : weather_description}
	
	return response


def fake_login():
	login_attempt = request.get_json()
	
	print(login_attempt)
	
	username = login_attempt['username']
	password = login_attempt['password']
	
	response = {}
	
	if username == 'epic_man_69' and password == "Password123":
		response = {'success': True}
	else:
		response = {'success': False}
		
	return jsonify(response)
	

def survived_titanic():
	features = request.get_json()
	
	survived = guess_if_survived(features['pclass'], 
								 features['sex'],
								 features['age'],
								 features['siblings'],
								 features['parents'],
								 features['fare_price'])
	
	response = {"survived": survived}
	
	return jsonify(response)
