# Import the 'requests' library to handle HTTP requests.
import requests


def get_weather(api_key, city):
    """
    Fetches and returns the weather data for a specified city using the OpenWeatherMap API.

    Args:
        api_key (str): The API key for accessing OpenWeatherMap.
        city (str): The name of the city for which to get the weather.

    Returns:
        dict: A dictionary containing the parsed weather data, or None if an error occurs.
    """
    # This is the base URL for the OpenWeatherMap current weather data API.
    base_url = "http://api.openweathermap.org/data/2.5/weather?"

    # Construct the complete URL with the city, API key, and desired units (metric for Celsius).
    # You can change 'metric' to 'imperial' for Fahrenheit.
    complete_url = f"{base_url}q={city}&appid={api_key}&units=metric"

    try:
        # Send a GET request to the API.
        response = requests.get(complete_url)

        # Raise an exception for bad status codes (4xx or 5xx).
        response.raise_for_status()

        # Convert the JSON response from the server into a Python dictionary.
        weather_data = response.json()

        # The API returns a code '404' in its JSON if the city is not found.
        if weather_data["cod"] != 200:
            print(f"Error: City '{city}' not found. Please check the spelling.")
            return None

        return weather_data

    except requests.exceptions.HTTPError as http_err:
        # Handle specific HTTP errors, like '401 Unauthorized' for a bad API key.
        if response.status_code == 401:
            print("Error: Invalid API key. Please check your key and try again.")
        else:
            print(f"An HTTP error occurred: {http_err}")
        return None
    except requests.exceptions.RequestException as err:
        # Handle other network-related errors (e.g., DNS failure, connection refused).
        print(f"An error occurred: {err}")
        return None


def display_weather(weather_data, city):
    """
    Formats and prints the weather data in a user-friendly way.

    Args:
        weather_data (dict): The dictionary of weather information.
        city (str): The name of the city, for display purposes.
    """
    if weather_data is None:
        return

    # Extract the required information from the 'main' section of the data.
    main_weather_info = weather_data["main"]
    temperature = main_weather_info["temp"]
    feels_like = main_weather_info["feels_like"]
    humidity = main_weather_info["humidity"]

    # Extract wind speed.
    wind_info = weather_data["wind"]
    wind_speed = wind_info["speed"]

    # The weather description is inside a list, so we get the first element.
    weather_description = weather_data["weather"][0]["description"]

    # Print the formatted weather report.
    print("\n" + "=" * 30)
    print(f"Weather Report for {city.title()}")
    print("=" * 30)
    print(f"  Description: {weather_description.title()}")
    print(f"  Temperature: {temperature}°C")
    print(f"  Feels Like:  {feels_like}°C")
    print(f"  Humidity:    {humidity}%")
    print(f"  Wind Speed:  {wind_speed} m/s")
    print("=" * 30 + "\n")


# --- Main Program Execution ---
if __name__ == "__main__":
    # IMPORTANT: Replace "YOUR_API_KEY_HERE" with your actual OpenWeatherMap API key.
    api_key = "4abc30698e039ab1349a28a60fe2b636"

    # Get the city name from the user.
    city_name = input("Enter a city name to get the weather forecast: ")

    # Call the function to get the weather data.
    current_weather_data = get_weather(api_key, city_name)

    # If data was successfully retrieved, display it.
    if current_weather_data:
        display_weather(current_weather_data, city_name)