import requests

# Replace with your OpenWeatherMap API key
API_KEY = "your_api_key_here"

def get_weather(location):
    """Fetch weather data from OpenWeatherMap API."""
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    
    # Detect if user entered ZIP code or city name
    if location.isdigit():
        params = {"zip": location, "appid": API_KEY, "units": "metric"}
    else:
        params = {"q": location, "appid": API_KEY, "units": "metric"}
    
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Raises error for bad HTTP status
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None

def display_weather(data):
    """Print weather details."""
    city = data['name']
    country = data['sys']['country']
    temp = data['main']['temp']
    humidity = data['main']['humidity']
    condition = data['weather'][0]['description'].title()

    print("\n--- Current Weather ---")
    print(f"Location   : {city}, {country}")
    print(f"Temperature: {temp}°C")
    print(f"Humidity   : {humidity}%")
    print(f"Condition  : {condition}")
    print("-----------------------")

def main():
    print("=== Simple Weather App ===")
    location = input("Enter city name or ZIP code: ").strip()

    if not location:
        print("Error: Location cannot be empty!")
        return

    data = get_weather(location)
    
    if data and data.get("cod") == 200:
        display_weather(data)
    else:
        print("Error: Could not retrieve weather data. Check location.")

if __name__ == "__main__":
    main()
