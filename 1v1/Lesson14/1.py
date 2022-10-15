from urllib import request, parse
from bs4 import BeautifulSoup

word = input('输入关键词: ')
keyword = parse.urlencode({"word": word})

html = request.urlopen(f'http://baike.baidu.com/search/word?{keyword}')
html = html.read()
soup = BeautifulSoup(html, "html.parser")
item_list = soup.find_all(class_='item')
for i in item_list:
    a = i.find('a')
    if a:
        href = a['href']
        print('http://baike.baidu.com' + href, a.text)