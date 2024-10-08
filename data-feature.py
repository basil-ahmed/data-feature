import requests
from IPython.display import Image, display

# Step 1: Get weather data using OpenWeatherMap API
def get_weather(city):
    api_key = "API_KEY"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(url)
    data = response.json()
    
    if response.status_code == 200:
        description = data['weather'][0]['description']
        return description
    else:
        print(f"Error: {data.get('message', 'Unable to fetch weather data')}")
        return None

# Step 2: Get image based on weather description using Pexels API
def get_image(query):
    api_key = "API_KEY"
    url = "https://api.pexels.com/v1/search"
    headers = {
        "Authorization": api_key
    }
    params = {
        "query": query,
        "per_page": 1
    }
    response = requests.get(url, headers=headers, params=params)
    data = response.json()

    if response.status_code == 200 and data['photos']:
        image_url = data['photos'][0]['src']['original']
        return image_url
    else:
        return None

# Main function: Pipeline of both APIs
def weather_image_pipeline(city):
    weather_description = get_weather(city)
    if weather_description:
        print(f"Weather in {city}: {weather_description}")
        image_url = get_image(weather_description + " in " + city)
        if image_url:
            print(f"Image based on '{weather_description}' in '{city}': {image_url}")
            display(Image(url=image_url))
        else:
            print(f"No image found for '{weather_description}'.")
    else:
        print(f"Couldn't retrieve weather data for '{city}'.")

# Example Usage
weather_image_pipeline("Boston")
