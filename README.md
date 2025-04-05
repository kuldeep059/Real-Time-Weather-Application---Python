# WeatherVista - Real-Time Weather Application

WeatherVista is a web application that provides real-time weather information for any city you search. It uses the OpenWeatherMap API to fetch current weather data and displays it in a clean and attractive user interface.

## Features

* **Real-Time Weather:** Fetches and displays current temperature, weather description, humidity, and wind speed.
* **User-Friendly Interface:** Attractive and responsive design with an animated background.
* **City Search:** Allows users to search for weather in any city.
* **Error Handling:** Displays clear error messages for invalid city names.
* **.env Support:** Uses a `.env` file to securely store your OpenWeatherMap API key.

## Technologies Used

* **Python:** Backend logic and API integration.
* **Flask:** Web framework for creating the application.
* **Requests:** For making HTTP requests to the OpenWeatherMap API.
* **python-dotenv:** For managing environment variables.
* **HTML/CSS:** Frontend design and layout.
* **OpenWeatherMap API:** For weather data.

## Prerequisites

Before running the application, ensure you have the following installed:

* Python 3.6+
* pip (Python package installer)

## Installation

1.  **Clone the repository:**

    ```bash
    git clone <repository_url>
    cd WeatherVista
    ```

2.  **Create a virtual environment (recommended):**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On macOS/Linux
    venv\Scripts\activate  # On Windows
    ```

3.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```
    (Create a requirements.txt file with:
    ```
    Flask
    requests
    python-dotenv
    ```
    )

4.  **Create a `.env` file:**

    Create a `.env` file in the root directory of the project and add your OpenWeatherMap API key:

    ```
    current_weather_data=YOUR_OPENWEATHERMAP_API_KEY
    ```

    Replace `YOUR_OPENWEATHERMAP_API_KEY` with your actual API key.

5.  **Run the application:**

    ```bash
    python app.py
    ```

6.  **Open your browser:**

    Open your web browser and go to `http://127.0.0.1:5000/`.

## Usage

1.  Enter the name of the city you want to get weather information for in the input field.
2.  Click the "Get Weather" button.
3.  The application will display the current weather information for the specified city.
4.  If the city is not found, an error message will be displayed.

## Contributing

Contributions are welcome! If you find any bugs or have suggestions for improvements, please feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
