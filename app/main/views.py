from flask import render_template, session, redirect, url_for, current_app,request
from . import main
import requests

@main.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')




@main.route('/city', methods=['GET', 'POST'])
def search_city():
    render_response = ""
    if(request.method == 'POST'):
        API_KEY = 'f4a57ea2b1b2a60a338eec44ed946015'  # initialize your key here
        city = request.form.get('city')  # city name passed as argument
        country = request.form.get('country')
        location = city + ", " +country
        # call API and convert response into Python dictionary
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&APPID={API_KEY}'
        response = requests.get(url).json()

        
        
        # error like unknown city name, inavalid api key
        if response.get('cod') != 200:
            message = response.get('message', '')
            render_response = f'Error getting temperature for {city.title()}. Error message = {message}'
        
        # get current temperature and convert it into Celsius
        current_temperature = response.get('main', {}).get('temp')
        if current_temperature:
            current_temperature_celsius = round(current_temperature - 273.15, 2)
            render_response = 'success'
        else:
            render_response = f'Error getting temperature for {city.title()}'
    return render_template('weather.html', render_response=render_response, location = location, current_temperature_celsius = current_temperature_celsius )
