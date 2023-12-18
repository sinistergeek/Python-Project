import requests
api_key = "Your_API_Key"
base_url = "http://api.openweathermap.org/data/2.5/weather?"
city_name = input("Enter city name")
complete_url = base_url + "appid=" + api_key + "&q=" + city_name
response = requests.get(complete_url)
x=response.json()


