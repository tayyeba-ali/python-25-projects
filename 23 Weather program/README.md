# 🌦️ Weather App (Python CLI)

A simple command-line weather application built using **Python** and the **OpenWeatherMap API**. Enter a city name and get real-time weather details like temperature, humidity, wind speed, and more.

---

## 🚀 Features

* Real-time weather updates for any city 🌍
* Displays:

  * Temperature and "feels like" value 🌡️
  * Weather description (e.g., clear sky, rain) ☁️
  * Humidity 💧
  * Wind speed 💨
* Easy-to-use CLI interface

---

## 💠 Requirements

* Python 3.x
* `requests` library
  Install using:

  ```
  pip install requests
  ```

---

## 🔑 Setup

1. Get your free API key from [OpenWeatherMap](https://openweathermap.org/api)
2. Replace the `API_Key` variable in the script:

   ```python
   API_Key = 'your_api_key_here'
   ```

---

## ▶️ Usage

Run the script in your terminal:

```bash
python weather_app.py
```

Then enter a city name when prompted:

```
🧱 Enter the city name: Lahore
📍 Weather in Lahore, PK:
🌡️ Temperature     : 33°C
🥵 Feels Like      : 35°C
🌤️ Weather         : Clear Sky
💧 Humidity        : 38%
💨 Wind Speed      : 2.5 m/s
```

---

## 📁 File Structure

```
weather_app.py
README.md
```

---

## 🙌 Acknowledgements

* [OpenWeatherMap](https://openweathermap.org/) for the weather data API

---

## 📜 License

This project is open-source and free to use.

---

> Built with ❤️ by Tayyeba Ali
