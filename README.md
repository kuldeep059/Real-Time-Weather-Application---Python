# WeatherVista - Real-Time Weather Application

WeatherVista is a web application that provides real-time weather information for any city you search. It uses the OpenWeatherMap API to fetch current weather data and displays it in a clean and attractive user interface.

## 🌟 Features

- **Real-Time Weather**: Fetches and displays current temperature, weather description, humidity, and wind speed.  
- **User-Friendly Interface**: Attractive and responsive design with an animated background.  
- **City Search**: Allows users to search for weather in any city.  
- **Error Handling**: Displays clear error messages for invalid city names.  
- **.env Support**: Uses a `.env` file to securely store your OpenWeatherMap API key.

## 🔧 Technologies Used

- **Python**: Backend logic and API integration  
- **Flask**: Web framework for creating the application  
- **Requests**: For making HTTP requests to the OpenWeatherMap API  
- **python-dotenv**: For managing environment variables  
- **HTML/CSS**: Frontend design and layout  
- **OpenWeatherMap API**: For weather data  

## 🧰 Prerequisites

Ensure you have the following installed:

- Python 3.6+  
- `pip` (Python package installer)

## 🚀 Installation

1. **Clone the repository**:
   ```bash
   git clone <repository_url>
   cd WeatherVista
## 🛠️ Setup Instructions

### ✅ Create a Virtual Environment (Recommended)
    ```bash
      python -m venv venv
      source venv/bin/activate  # On macOS/Linux
      venv\Scripts\activate     # On Windows

## ☁️ Azure Cloud Deployment and DevOps Integration

**WeatherVista** is deployed on **Microsoft Azure App Service** with end-to-end DevOps implementation.

---

### ✅ Cloud Infrastructure & Deployment Using Azure

- Hosted on Azure App Service  
- 🌐 **Live Link**: [WeatherVista](https://weather-vista-h9gqe0ehf2b9e6ac.eastus-01.azurewebsites.net)  
- Deployment is done using GitHub CI/CD workflows.

---

### 🔄 CI / CD Pipeline

- **GitHub Actions**: Automatically builds and deploys on every push to the main branch.  
- **Zero downtime deployment** with integrated build steps.

---

### 🔐 Security & Compliance

- **Environment Variables**: API keys and secrets are securely stored in **Azure Application Settings**, not in the code repository.  
- No sensitive data checked into version control.

---

### 📊 Monitoring & Logging

- **Azure Monitoring Enabled**: View real-time logs in:
  - **KUDU (Advanced Tools)**
  - **Azure App Service > Logs** section  
- Application health and error tracking are turned on for better observability.

---

### 🗃️ Database and Storage Management

- While this app doesn't require a database, the infrastructure supports integration with **Azure Storage** or **Azure SQL** for future enhancements.

---

### 📈 Log Analysis & Automation

- Application logs are archived and can be used with **Azure Log Analytics**.  
- **Automated alerts** can be configured for error patterns or high latency.

---

### 🧪 Future Improvements

- 5-day weather forecast integration  
- Location-based weather detection  
- Weather icons and improved animations  
- Mobile-first enhancements

---

Feel free to **fork**, **star**, and **contribute** to this project! 😊  
For any questions or feature requests, raise an issue or contact via GitHub.
