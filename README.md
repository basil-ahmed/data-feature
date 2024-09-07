# Weather Image Pipeline

This Python script creates a data feature that retrieves the current weather for a specified city and displays an image related to that weather. It leverages the **OpenWeatherMap API** to get weather data and the **Pexels API** to fetch relevant images.

## Features
- Get real-time weather data for a city.
- Retrieve images based on the weather description.
- Display the image in a Jupyter Notebook.

## APIs Used
- **OpenWeatherMap API**: Provides real-time weather data such as temperature, weather description, and more.
- **Pexels API**: Fetches high-quality images based on search queries, in this case, weather descriptions.

### Why These APIs Were Chosen
- **OpenWeatherMap** offers reliable, real-time weather information for cities globally.
- **Pexels** is known for its large library of free, high-quality images, making it perfect for visual representation.

## Purpose
This feature allows users to visualize weather conditions for any city by displaying a relevant image based on the current weather, enhancing both user experience and engagement in weather-based applications.

## How It Works
1. **Weather API Call**: The script retrieves a city's current weather description.
2. **Image API Call**: Using the weather description, the script fetches an image from the Pexels API to visually represent the weather.
3. **Display**: The image is displayed in a Jupyter Notebook or any Python environment that supports image display.

## Prerequisites
1. Python 3.x installed.
2. Necessary libraries:
   ```bash
   pip install requests IPython
   ```
3. API Keys:
   - OpenWeatherMap API key [Sign up here](https://home.openweathermap.org/users/sign_up)
   - Pexels API key [Sign up here](https://www.pexels.com/api/)

## Setup
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/weather-image-pipeline.git
   cd weather-image-pipeline
   ```

2. Replace the placeholder API keys in the script with your own keys.

3. Example usage:
   ```python
   weather_image_pipeline("Boston")
   ```

## Instructions
1. **OpenWeatherMap**: Sign up and obtain an API key. Update the `get_weather()` function with your key.
2. **Pexels**: Sign up and obtain an API key. Update the `get_image()` function with your key.
3. Run the script in a Jupyter notebook or a Python environment that supports image display.

## Code Explanation

### Step 1: Get Weather Data
The function `get_weather()` takes the name of a city and retrieves its current weather description using the OpenWeatherMap API.
```python
def get_weather(city):
    api_key = "YOUR_OPENWEATHERMAP_API_KEY"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        description = response.json()['weather'][0]['description']
        return description
    else:
        return None
```

### Step 2: Get an Image from Pexels
The `get_image()` function uses the weather description as a search query and fetches an image using the Pexels API.
```python
def get_image(query):
    api_key = "YOUR_PEXELS_API_KEY"
    url = "https://api.pexels.com/v1/search"
    headers = {"Authorization": api_key}
    params = {"query": query, "per_page": 1}
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200 and response.json()['photos']:
        return response.json()['photos'][0]['src']['original']
    else:
        return None
```

### Step 3: Pipeline Function
The `weather_image_pipeline()` function connects both APIs. It first gets the weather description, then uses that to fetch and display an image related to the weather.
```python
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
```

## Usage
To use this code, simply call the `weather_image_pipeline()` function with the name of the city as the argument:
```python
weather_image_pipeline("Boston")
```

## Example Output
```bash
Weather in Boston: light rain
Image based on 'light rain' in 'Boston': [Image URL displayed]
```

## Error Handling
The script handles errors such as:
- Invalid city names.
- API request limits.
- Missing or incomplete data.

## License
This project is licensed under the MIT License.
