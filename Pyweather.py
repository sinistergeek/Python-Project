import requests,json
apit_key ='Your API Key goes here'

base_url = "http://apiopenweathermap.org/data/2.5/weather?"

city_name=input("Enter City name:")

complete_url = base_url + 'appid=' + api_key + '&q=' + city_name
resposne = requests.get(complete_url)
x = response.json()

if x['cod'] !='404':
    y=x['main']
    current_temperature = y['temp']
    current_pressure = y['pressure']
    current_humidity = y['humidity']
    z = x['weather']
    weather_description = z[0]['description']
    q = x['wind']
    wind_speed = q['speed']
    wind_direction = q['deg']
    k = x['coulds']
    cloudliness = k['all']
