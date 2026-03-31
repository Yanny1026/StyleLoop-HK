import requests
import json

def get_current_weather():
    """
    Fetches current weather data from Hong Kong Observatory API.
    Returns a dictionary with average temperature and humidity.
    """
    url = "https://data.weather.gov.hk/weatherAPI/opendata/weather.php?dataType=rhrread&lang=en"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        
        # Extract temperature data
        temp_data = data.get('temperature', {}).get('data', [])
        temps = [item['value'] for item in temp_data if 'value' in item]
        avg_temp = sum(temps) / len(temps) if temps else None
        
        # Extract humidity data
        humidity_data = data.get('humidity', {}).get('data', [])
        humidities = [item['value'] for item in humidity_data if 'value' in item]
        avg_humidity = sum(humidities) / len(humidities) if humidities else None
        
        return {
            'temperature': avg_temp,
            'humidity': avg_humidity
        }
    except requests.RequestException as e:
        print(f"Error fetching weather data: {e}")
        return None