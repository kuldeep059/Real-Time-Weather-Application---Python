from flask import Flask, render_template, request
import requests
import os
import logging
from datetime import datetime
from dotenv import load_dotenv

# Load .env variables (if running locally)
load_dotenv()

# Initialize Flask app
app = Flask(__name__)

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(name)s: %(message)s',
)
logger = logging.getLogger(__name__)

# Get API key
user_api = os.environ.get('current_weather_data')

if not user_api:
    logger.error("API key not found. Please set the 'current_weather_data' environment variable.")
    exit()

# Weather fetch logic
def get_weather(location):
    logger.info(f"Fetching weather for location: {location}")
    complete_api_link = f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={user_api}"

    try:
        api_link = requests.get(complete_api_link)
        api_data = api_link.json()
    except Exception as e:
        logger.error(f"Error during API request: {e}")
        return None

    if api_data.get('cod') == '404':
        logger.warning(f"City '{location}' not found.")
        return None
    else:
        temp_city = api_data['main']['temp'] - 273.15
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

        logger.info(f"Weather data fetched successfully for {location}")
        return weather_data

# Route for homepage
@app.route('/', methods=['GET', 'POST'])
def index():
    weather_info = None
    error_message = None

    if request.method == 'POST':
        location = request.form.get('city')
        if location:
            weather_info = get_weather(location)
            if weather_info is None:
                error_message = f"City '{location}' not found."
        else:
            error_message = "Please enter a city name."

    return render_template('index.html', weather_info=weather_info, error_message=error_message)

# Main entry
if __name__ == '__main__':
    app.run(debug=True)
