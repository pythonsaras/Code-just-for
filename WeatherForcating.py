import requests,json

api_key="74d4501738e18efa9a59af7dfaa82e06"

base_url="https://api.openweathermap.org/data/2.5/weather?"
city_name=input()

complete_url=base_url+"appid="+api_key+"&q="+city_name
response=requests.get(complete_url)
x=response.json()

if ["cod"]!="404":
    y=x["main"]

    current_temp=y["temp"]
    current_pressure=y["pressure"]
    current_humidity=y["humidity"]

    z=x["weather"]

    weather_description=z[0]["description"]
    print(f"Temperature {(current_temp-273.15)} Humidity is {current_humidity} Pressure is {round(0.0009869233 *current_pressure)} Description {weather_description}")
else:
    print("City not found")
