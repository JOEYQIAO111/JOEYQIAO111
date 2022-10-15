#from bs4 import BeautifulSoup
html = '''
<html>
    <head>
        <title>The Dormouse's story</title>
    </head>
    <body>
        <p class="story">
            Once upon a time there were three little sisters; and their names were
            <a href="http://example.com/elsie" class="sister" id="link1">
                <span>Elsie</span>
            </a>
            <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> 
            and
            <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>
            and they lived at the bottom of a well.
        </p>
        <p class="story">...</p>
'''

'''print(soup.a.attrs)
print(type(soup.head))
print(soup.p.contents)

L = soup.find_all(class_ = 'sister')
print(L)'''

#print(soup.select('p a span')[0].string)

html = '''<div class="panel">
    <div class="panel-heading">
        <h4>Hello</h4>
    </div>
    <div class="panel-body">
        <ul class="list" id="list-1">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
            <li class="element">Jay</li>
        </ul>
        <ul class="list list-small" id="list-2">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
        </ul>
    </div>
</div>'''

'''soup = BeautifulSoup(html)
L = soup.select('div li')
for i in range(len(L)):
    print(L[i].string)'''
'''import requests
from bs4 import BeautifulSoup
headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'}
url = requests.get('https://www.baidu.com/')
#url.encoding = url.apparent_encoding
print(url.text)'''

'''import requests
from bs4 import BeautifulSoup
url = requests.get('https://www.cas.cn/kxyj/cb/qk/')
url.encoding = url.apparent_encoding
f = open('1.txt','w')
f.write(url.text)
text = open('1.txt').read()
soup = BeautifulSoup(text)
L = soup.find('ul',class_= 'gl_list2 gl_list_qk').find_all('li')'''

# 中国天气网
import requests
from bs4 import BeautifulSoup
url = requests.get('http://www.weather.com.cn/weather/101010100.shtml')
url.encoding = url.apparent_encoding
f = open('中国天气网北京.txt','w', encoding = 'utf-8')
f.write(url.text)
text = open('中国天气网北京.txt', encoding = 'utf-8').read()
soup = BeautifulSoup(text)
L = soup.find_all('ul',class_= 't clearfix')[0]

for i in range(len(L.find_all('li'))):
    li_label = L.find_all('li')[i]
    date = li_label.find_all('h1')[0].string
    weather = li_label.find_all('p')[0].string
    temp = li_label.find_all('i')[0].string
    wind = li_label.find_all('i')[1].string
    print(date, ' ', weather, ' ', temp, ' ', wind)