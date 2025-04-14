from flask import Flask, render_template, request
import requests
import os
from datetime import datetime
from dotenv import load_dotenv

app = Flask(__name__)

user_api = os.environ.get('current_weather_data')

if not user_api:
    print("Error: API key not found. Please set the 'current_weather_data' environment variable.")
    exit()

def get_weather(location):
    complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q=" + location + "&appid=" + user_api
    api_link = requests.get(complete_api_link)
    api_data = api_link.json()

    if api_data['cod'] == '404':
        return None
    else:
        temp_city = ((api_data['main']['temp']) - 273.15)
        weather_desc = api_data['weather'][0]['description']
        hmdt = api_data['main']['humidity']
        wind_spd = api_data['wind']['speed']
        date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

        weather_data = {
            'location': location.upper(),
            'date_time': date_time,
            'temp_city': "{:.2f}".format(temp_city),
            'weather_desc': weather_desc,
            'hmdt': hmdt,
            'wind_spd': wind_spd,
        }
        return weather_data

@app.route('/', methods=['GET', 'POST'])
def index():
    weather_info = None
    error_message = None

    if request.method == 'POST':
        location = request.form['city']
        weather_info = get_weather(location)
        if weather_info is None:
            error_message = f"City '{location}' not found."

    return render_template('index.html', weather_info=weather_info, error_message=error_message)

if __name__ == '__main__':
    app.run(debug=True)
