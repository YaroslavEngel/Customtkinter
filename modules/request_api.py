import requests
#Імпортування функції read_json
from .read_json import read_json
#Імпортування модуля json
import json
#Додавання значень у файл confin_api.json
data_api = read_json(name_file= 'config_api.json')
#API ключ
API_KEY = data_api['api_key']
#Назва міста
CITY_NAME = data_api['city_name']
#URL силка до openweather
URL = f"https://api.openweathermap.org/data/2.5/weather?q={CITY_NAME}&appid={API_KEY}"
#Відповідь запросу на отримання URL силки
response = requests.get(URL)
#Код статуса
if response.status_code == 200:
    #Загрузка контента з буфера обміна
    data_dict = json.loads(response.content)
    #більш красиве відображення коду
    print(json.dumps(data_dict, indent= 4))