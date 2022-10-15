import requests
from lxml import etree

html = requests.get('https://www.thefreedictionary.com/5-letter-words.htm')
html = etree.HTML(html.text)

li = html.xpath('//*[@id="dCont"]/div[1]/ul/li[*]/a/@href')

list1 = []

for i in li:
    list1.append(i)

print(list1)