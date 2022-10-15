import requests
from bs4 import BeautifulSoup
# 这里可以加入列表的循环，循环访问每个链接
html = requests.get('http://book.zongheng.com/chapter/1169984/67173965.html')
soup = BeautifulSoup(html.text, "html.parser")
content = soup.find_all('p')
for i in content:
    print(i.string)