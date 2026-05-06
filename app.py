from flask import Flask, render_template, request
import requests

app = Flask(__name__)

GEOCODE_URL = "https://geocoding-api.open-meteo.com/v1/search"
WEATHER_URL = "https://api.open-meteo.com/v1/forecast"
ICON_URL = "https://openweathermap.org/img/wn/{icon}@2x.png"

WEATHER_CODE_DESCRIPTIONS = {
    0: "Clear sky",
    1: "Mainly clear",
    2: "Partly cloudy",
    3: "Overcast",
    45: "Fog",
    48: "Depositing rime fog",
    51: "Light drizzle",
    53: "Moderate drizzle",
    55: "Dense drizzle",
    56: "Freezing drizzle",
    57: "Freezing drizzle",
    61: "Slight rain",
    63: "Moderate rain",
    65: "Heavy rain",
    66: "Freezing rain",
    67: "Heavy freezing rain",
    71: "Light snow",
    73: "Moderate snow",
    75: "Heavy snow",
    77: "Snow grains",
    80: "Rain showers",
    81: "Moderate rain showers",
    82: "Heavy rain showers",
    85: "Snow showers",
    86: "Heavy snow showers",
    95: "Thunderstorm",
    96: "Thunderstorm with hail",
    99: "Thunderstorm with hail"
}

WEATHER_CODE_ICONS = {
    0: "01d",
    1: "02d",
    2: "03d",
    3: "04d",
    45: "50d",
    48: "50d",
    51: "09d",
    53: "09d",
    55: "09d",
    56: "13d",
    57: "13d",
    61: "10d",
    63: "10d",
    65: "10d",
    66: "13d",
    67: "13d",
    71: "13d",
    73: "13d",
    75: "13d",
    77: "13d",
    80: "09d",
    81: "09d",
    82: "09d",
    85: "13d",
    86: "13d",
    95: "11d",
    96: "11d",
    99: "11d"
}


def find_location(city: str):
    params = {
        "name": city,
        "count": 1,
        "language": "en",
        "format": "json"
    }
    response = requests.get(GEOCODE_URL, params=params, timeout=10)
    if response.status_code != 200:
        return None, "Unable to find location."

    data = response.json()
    results = data.get("results")
    if not results:
        return None, "City not found."

    return results[0], None


def get_weather(city: str):
    location, error = find_location(city)
    if error:
        return None, error

    params = {
        "latitude": location["latitude"],
        "longitude": location["longitude"],
        "current_weather": True,
        "timezone": "auto"
    }
    response = requests.get(WEATHER_URL, params=params, timeout=10)
    if response.status_code != 200:
        return None, "Unable to fetch weather data."

    data = response.json()
    current = data.get("current_weather")
    if not current:
        return None, "No current weather data available."

    weather_code = current.get("weathercode", 0)
    return {
        "city": location.get("name", city),
        "country": location.get("country", ""),
        "temperature": round(current.get("temperature", 0)),
        "description": WEATHER_CODE_DESCRIPTIONS.get(weather_code, "Weather"),
        "icon_url": ICON_URL.format(icon=WEATHER_CODE_ICONS.get(weather_code, "03d")),
        "humidity": "N/A",
        "wind_speed": current.get("windspeed", "N/A")
    }, None


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/weather", methods=["POST"])
def weather():
    city = request.form.get("city", "").strip()
    if not city:
        return render_template("index.html", error="Please enter a city name.")

    weather_data, error = get_weather(city)
    if error:
        return render_template("index.html", error=error)

    return render_template("weather.html", weather=weather_data)


if __name__ == "__main__":
    app.run(debug=True)
