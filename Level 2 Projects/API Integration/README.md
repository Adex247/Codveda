# API Integration Script

A Python script that fetches and displays live data from two free, public APIs — no API keys required.

## Features

- **Cryptocurrency prices** — fetches current prices for Bitcoin, Ethereum, and Dogecoin via the [CoinGecko API](https://www.coingecko.com/en/api).
- **Weather lookup** — geocodes a city name and fetches current weather conditions via the [Open-Meteo API](https://open-meteo.com/).
- Clean, formatted console output.
- Robust error handling for timeouts, connection issues, HTTP errors, and invalid responses.

## Requirements

- Python 3.7+
- [`requests`](https://pypi.org/project/requests/) library

## Installation

```bash
pip install requests
```

## Usage

```bash
python task3_api_integration.py
```

The script will:
1. Print current prices for Bitcoin, Ethereum, and Dogecoin in USD.
2. Prompt you for a city name (press Enter to default to Lagos) and print the current weather there.

### Example output

```
=== Cryptocurrency Prices ===
  Bitcoin    -> 63,250.00 USD
  Ethereum   -> 3,120.45 USD
  Dogecoin   -> 0.15 USD

Enter a city name for weather (or press Enter for 'Lagos'):

=== Weather for Lagos, Nigeria ===
  Temperature : 29.0 °C
  Wind speed  : 12.3 km/h
  Conditions  : Partly cloudy
```

## Error Handling

The script gracefully handles:
- Request timeouts
- Connection failures
- HTTP errors (4xx/5xx responses)
- Invalid/malformed JSON responses
- Empty or unrecognized API results (e.g. an unknown city name)

## Project Structure

```
.
├── task3_api_integration.py   # Main script
└── README.md                  # This file
```

## License

This project is for educational purposes.
