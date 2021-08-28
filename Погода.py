import requests
city = input('Введи город: ')
param = {'q': city,
         'APPID': '11c0d3dc6093f7442898ee49d2430d20',
         'units': 'metric',
         'lang': 'ru'}
weather = requests.get('https://api.openweathermap.org/data/2.5/weather', params=param)

data = weather.json()
template = 'Текущая температура в {} равна {}, {}, Ощущается как {}'
print(template.format(city, data["main"]["temp"], data['weather'][0]['description'], data['main']['feels_like']))
