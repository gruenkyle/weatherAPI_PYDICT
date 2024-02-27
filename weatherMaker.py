import requests

APIKEY = "2829dfada9e27e8d9b3de6f67d1b432a"
cities = 'Fresno'

url = f'http://api.openweathermap.org/data/2.5/weather?q={cities}&appid={APIKEY}'

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    temp = data['main']['temp']
    desc = data['weather'][0]['description']

    print (f'Temperature: {temp} K')
    print (f'Description: {desc}')

else:
    print(f"Error Fetching Weather Data")