#!/usr/bin/env python3
"""
StyleLoop HK Weather-Based Clothing Suggestion Script

This script fetches current weather data from Hong Kong Observatory
and provides clothing category suggestions based on temperature and humidity.
"""

from weather import get_current_weather
from suggestions import suggest_clothing_categories

def main():
    print("Fetching current weather data from Hong Kong Observatory...")
    
    weather = get_current_weather()
    
    if weather:
        temp = weather['temperature']
        humidity = weather['humidity']
        
        print(f"Temperature: {temp:.1f}°C")
        print(f"Humidity: {humidity:.1f}%")        
        print("\nClothing suggestions:")
        suggestions = suggest_clothing_categories(temp, humidity)
        
        for suggestion in suggestions:
            print(f"- {suggestion}")
    else:
        print("Failed to retrieve weather data. Please check your internet connection.")

if __name__ == "__main__":
    main()