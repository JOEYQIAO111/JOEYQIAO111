import requests
from bs4 import BeautifulSoup

html = requests.get('http://www.weather.com.cn/weather/101010100.shtml')
html.encoding = 'utf-8'

soup = BeautifulSoup(html.text, 'html.parser')
li = soup.find_all('li', class_='sky')

print('盗版中国天气网')
print('--------------------------------------------------------------------------------')

for i in li:
    date = i.find('h1').text
    weather = i.find('p', class_='wea').text
    temp = i.find('p', class_='tem')
    high_temp = temp.find('span').text
    low_temp = temp.find('i').text
    print(date)
    print(weather)
    print(high_temp+'-'+low_temp)
    print('--------------------------------------------------------------------------------')