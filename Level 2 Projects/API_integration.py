"""
Task 3: API Integration
------------------------
Fetches and displays live data from two public APIs:
  1. Cryptocurrency prices  -> CoinGecko API   (no API key required)
  2. Weather for a city     -> Open-Meteo API  (no API key required)

Objectives covered:
  - Uses the `requests` library to make GET requests to an API.
  - Parses and displays the fetched data in a user-friendly format.
  - Handles errors, such as failed requests or invalid responses.
"""

import requests

CRYPTO_URL = "https://api.coingecko.com/api/v3/simple/price"
GEOCODE_URL = "https://geocoding-api.open-meteo.com/v1/search"
WEATHER_URL = "https://api.open-meteo.com/v1/forecast"

# Open-Meteo weather codes -> human-readable description
WEATHER_CODES = {
    0: "Clear sky", 1: "Mainly clear", 2: "Partly cloudy", 3: "Overcast",
    45: "Fog", 48: "Depositing rime fog",
    51: "Light drizzle", 53: "Moderate drizzle", 55: "Dense drizzle",
    61: "Slight rain", 63: "Moderate rain", 65: "Heavy rain",
    71: "Slight snow", 73: "Moderate snow", 75: "Heavy snow",
    80: "Rain showers", 95: "Thunderstorm",
}


def get_crypto_prices(coins, currency="usd"):
    """Fetch current prices for a list of cryptocurrency ids."""
    params = {
        "ids": ",".join(coins),
        "vs_currencies": currency,
    }

    try:
        response = requests.get(CRYPTO_URL, params=params, timeout=10)
        response.raise_for_status()  # raises HTTPError for 4xx/5xx responses
    except requests.exceptions.Timeout:
        print("Error: The request to the crypto API timed out.")
        return None
    except requests.exceptions.ConnectionError:
        print("Error: Could not connect to the crypto API. Check your internet connection.")
        return None
    except requests.exceptions.HTTPError as err:
        print(f"Error: Crypto API returned an HTTP error - {err}")
        return None
    except requests.exceptions.RequestException as err:
        print(f"Error: An unexpected request error occurred - {err}")
        return None

    try:
        data = response.json()
    except ValueError:
        print("Error: Crypto API response was not valid JSON.")
        return None

    if not data:
        print("Error: No data returned. Check that the coin names are valid.")
        return None

    return data


def display_crypto_prices(data, currency="usd"):
    """Print cryptocurrency prices in a readable format."""
    print("\n=== Cryptocurrency Prices ===")
    for coin, prices in data.items():
        price = prices.get(currency)
        if price is None:
            print(f"  {coin.capitalize():<10} -> price unavailable")
        else:
            print(f"  {coin.capitalize():<10} -> {price:,.2f} {currency.upper()}")


def get_coordinates(city_name):
    """Look up latitude/longitude for a city name."""
    params = {"name": city_name, "count": 1}

    try:
        response = requests.get(GEOCODE_URL, params=params, timeout=10)
        response.raise_for_status()
    except requests.exceptions.RequestException as err:
        print(f"Error: Could not look up city '{city_name}' - {err}")
        return None

    try:
        data = response.json()
    except ValueError:
        print("Error: Geocoding API response was not valid JSON.")
        return None

    results = data.get("results")
    if not results:
        print(f"Error: No location found for '{city_name}'. Check the spelling.")
        return None

    top = results[0]
    return top["latitude"], top["longitude"], top.get("name", city_name), top.get("country", "")


def get_weather(latitude, longitude):
    """Fetch current weather for given coordinates."""
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current_weather": True,
    }

    try:
        response = requests.get(WEATHER_URL, params=params, timeout=10)
        response.raise_for_status()
    except requests.exceptions.RequestException as err:
        print(f"Error: Could not fetch weather data - {err}")
        return None

    try:
        data = response.json()
    except ValueError:
        print("Error: Weather API response was not valid JSON.")
        return None

    current = data.get("current_weather")
    if not current:
        print("Error: Weather data missing from response.")
        return None

    return current


def display_weather(city_display_name, country, weather):
    """Print weather data in a readable format."""
    description = WEATHER_CODES.get(weather.get("weathercode"), "Unknown conditions")
    print(f"\n=== Weather for {city_display_name}, {country} ===")
    print(f"  Temperature : {weather.get('temperature')} °C")
    print(f"  Wind speed  : {weather.get('windspeed')} km/h")
    print(f"  Conditions  : {description}")


def main():
    # --- Cryptocurrency section ---
    coins = ["bitcoin", "ethereum", "dogecoin"]
    crypto_data = get_crypto_prices(coins)
    if crypto_data:
        display_crypto_prices(crypto_data)

    # --- Weather section ---
    city = input("\nEnter a city name for weather (or press Enter for 'Lagos'): ").strip()
    if not city:
        city = "Lagos"

    location = get_coordinates(city)
    if location:
        lat, lon, name, country = location
        weather = get_weather(lat, lon)
        if weather:
            display_weather(name, country, weather)


if __name__ == "__main__":
    main()