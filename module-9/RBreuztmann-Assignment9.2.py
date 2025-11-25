# Breutzmann, Robert
# CSD 325 - Advanced Python
# Due Date - 11/30/2025

import requests
import json

while True:
    zipcode = input("Enter the ZipCode for the forecast you are looking for: ")
    
    # Convert Zipcode to Lat/Long for Weather API
    lat_long = requests.get(f"https://api.zippopotam.us/us/{zipcode}")
    print("\nTesting ZIP API connection...")
    print("Status Code:", lat_long.status_code)

    if lat_long.status_code == 200: # If the Zipcode comes back clean
        print("\nRaw ZIP API Response:")
        print(lat_long.text)
        lat_long = lat_long.json()
        lat = lat_long["places"][0]["latitude"]
        long = lat_long["places"][0]["longitude"]
        print(f"\nCoordinates for {zipcode}: {lat}, {long}")

        city = lat_long["places"][0]["place name"]
        state = lat_long["places"][0]["state"]
        location = f"{city}, {state}"

    else:
        print("There was an error with that ZIP code.  Try again")
        continue
    
    # points on the weather.gov API used lat,long to pinpoint location.
    pointsURL = f"https://api.weather.gov/points/{lat},{long}"
    points = requests.get(pointsURL)

    print("\nTesting weather.gov connection...")
    print("Status Code:", points.status_code)
    if points.status_code == 200: # If data returns
        pointsData = points.json()
        forecastURL = pointsData["properties"]["forecast"]
        print(f"\nForecast URL: {forecastURL}")

        forecast=requests.get(forecastURL)
        # print("\nRaw Forecast Response:")
        # print(forecast.text)

        # This will print the forecast in a readable way.
        forecastData = forecast.json()
        print(f"\nReadable Forecast for {location}:")
        periods = forecastData["properties"]["periods"]

        for p in periods:
            print("------------------------------")
            print(f"{p['name']}")
            print(f"Temp: {p['temperature']}°{p['temperatureUnit']}")
            print(f"Wind: {p['windSpeed']} {p['windDirection']}")
            print(f"Forecast: {p['shortForecast']}")
            print()


    else:
        print("Error retrieving Weather Data.")


    again = input("Would you like to check another location? (y/n)")
    again = again[0].strip().lower()
    if again == "n":
        print("Thanks for using Bobs's Weather Checker App.")
        break