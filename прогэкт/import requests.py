import requests

weather_token = '6e8d79779a0c362f14c60a1c7f363e29'

city = input('Name of city:')

response = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={weather_token}&units=metric")
data = response.json()
city = data['name']
temperature = round(data['main']['temp'])
humidity = round(data['main']['humidity'])
wind = round(data['main']['wind'])

try:
    f('Привітик!\n Що в нас по погоді:\n\n')
    f('')


    print(response.json())
except:
    print('Здається, ви помилились :(')