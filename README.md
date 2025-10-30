# Weather Scraper
A Python script that scrapes current weather conditions from the National Weather Service (weather.gov) for any US location.

## Features
Fetches real-time weather data for any US coordinates
- Displays temperature in both Fahrenheit and Celsius
- Shows current weather conditions
- Robust error handling for network and parsing errors
- Clean, formatted terminal output with bold labels

## Requirements
```
bashpip install requests beautifulsoup4
```
## Usage
Basic Usage
```
pythonpython weather_scraper.py
```
This fetches weather for NYC (default coordinates: 40.7678°N, 73.9645°W)

Custom Location
```
pythonfrom weather_scraper import get_weather

# Los Angeles
get_weather(lat=34.0522, lon=-118.2437)

# Chicago
get_weather(lat=41.8781, lon=-87.6298)
```
Example Output
```
Location:
  Lat: 40.77°N 
  Lon: 73.96°W 
  Elev: 154 ft.

Current Weather:
  Temperature: 56°F / 13°C
  Conditions: Fog/Mist
```  
## How It Works
- Constructs URL with latitude/longitude coordinates
- Sends HTTP request to weather.gov with 10-second timeout
- Parses HTML using BeautifulSoup to extract weather data
- Formats and displays location and current conditions

## Error Handling
The script handles:
- Network errors: Connection failures, timeouts, HTTP errors
- Parsing errors: Missing HTML elements, structure changes
- Invalid data: Checks if weather elements exist before accessing

## Limitations
- Only works for US locations (weather.gov coverage area)
- Scrapes HTML structure which may change without notice
- No caching - fetches fresh data on every request
- Subject to weather.gov's terms of service and rate limits

## Finding Coordinates
To find coordinates for any location:
- Go to https://weather.gov
- Search for your location
- Click on a point on the map
- Copy the lat/lon from the URL

## Disclaimer
This script scrapes data from weather.gov for personal/educational use. Please be respectful:
- Don't make excessive requests
- Consider caching results  
- Check weather.gov's terms of service before any production use

Data accuracy and availability depends on weather.gov's service.