import requests
from api_key import API_KEY

def weather(url):
    response = requests.get(url)
    data = response.json()
    print('Temperature:', data['main']['temp'], 'K')
    print('Condition:', data['weather'][0]['description'])
    print('Humidity:', data['main']['humidity'], '%')
    print('Wind speed:', data['wind']['speed'], 'm/s')

print('Welcome to the Weather Forecast App!')

choice = input('Will you enter city name or coordinates:').lower()

if choice == 'city name':

    


    BASE_URL = 'http://api.openweathermap.org/data/2.5/'


    ENDPOINT = 'weather'


    CITY_NAME = input('Enter a city name: ').lower()

    url = f'{BASE_URL}{ENDPOINT}?q={CITY_NAME}&appid={API_KEY}'


    weather(url)

elif choice == 'coordinates':


    BASE_URL = 'http://api.openweathermap.org/data/2.5/'


    ENDPOINT = 'weather'


    lat = input('Enter lat: ')
    lon = input('Enter lon: ')


    url = f'{BASE_URL}{ENDPOINT}?lat={lat}&lon={lon}&appid={API_KEY}'


    weather()

else:
    print('invalid choice')    