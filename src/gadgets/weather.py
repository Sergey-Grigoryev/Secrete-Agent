import requests
import os


def get_weather(location):

    # Spoofed weather and temperature
    weather = "Sunny"
    temperature = 25

    # Enable and update the following code to fetch real weather data

    # Use your OpenWeatherMap API key
    API_KEY = os.getenv("OPENWEATHER_API_KEY")
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={API_KEY}&units=metric"

    try:
        # Send a GET request to the weather API
        response = requests.get(url)
        data = response.json()

        # Check if the API returned a valid response
        if data["cod"] == 200:
            weather = data["weather"][0]["description"]
            temperature = data["main"]["temp"]
            return f"Weather in {location}: {weather}, {temperature}°C"
        else:
            return f"Error: Could not retrieve weather for {location}. Reason: {data.get('message', 'Unknown error')}."

    except Exception as e:
        return f"Error: Failed to retrieve weather data. Details: {e}"
