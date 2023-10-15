import requests
import json

city = "Seoul" #도시
apiKey = "a925fba4ba02e326018e5bac4fcaef54"
lang = 'kr' #언어
units = 'metric' #화씨 온도를 섭씨 온도로 변경
api = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={apiKey}&lang={lang}&units={units}"
#api = f"https://api.openweathermap.org/data/2.5/weather?lat=${lat}&lon=${lon}&appid=${API_KEY}&units=metric"
result = requests.get(api)
result = json.loads(result.text)

name = result['name']
lon = result['coord']['lon']
lat = result['coord']['lat']
windpower = result['wind']['speed']
temperature = result['main']['temp']
humidity = result['main']['humidity']

print(name)
print(lon, ', ', lat)
print(windpower)#풍속
print(temperature) #온도
print(humidity) #습도