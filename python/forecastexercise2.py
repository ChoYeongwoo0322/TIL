import requests
from pprint import pprint
url = 'https://www.metaweather.com/api/location/1132447/'
res = requests.get(url).json()
#pprint(res)
# pprint(res['consolidated_weather'])
forecast_list = res['consolidated_weather']
#반복해야함
for forecast in forecast_list:
    # pprint(forecast)
    print(f'{forecast["applicable_date"]} 날씨')
    print(f'날씨 : {forecast["weather_state_name"]}')
    print(f'최고기온 : {forecast["max_temp"]}')
    print(f'최저기온 : {forecast["min_temp"]}')
    print(f'습도 : {forecast["humidity"]}')
    print(f'풍속 : {forecast["wind_speed"]}')
    print('---------------')

print(type(res))