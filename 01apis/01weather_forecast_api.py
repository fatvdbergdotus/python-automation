import requests

fatvdbergdotus_open_weather_forecast_api = "84e136836b5e9638f2e089558687f86a"
lat = 44.34
lon = 10.99

# get the weather forecast data from the OpenWeatherMap API
url = f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={fatvdbergdotus_open_weather_forecast_api}"
r= requests.get(url)
content = r.json()

# write the weather forecast data to a CSV file
with open("weather_forecast.csv", "w") as f:
    f.write("Date and time,Temperature (K),Weather description\n")

    for item in content["list"]:    
        f.write(f"{item['dt_txt']},{item['main']['temp']},{item['weather'][0]['description']}\n")