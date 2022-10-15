import requests
from lxml import etree

headers = {
    'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 OPR/82.0.4227.50'
}

html = requests.get('https://blog.csdn.net/qq_42554007', headers = headers).text
html = etree.HTML(html)

path = html.xpath("//article/a/@href")
title_path = html.xpath("//article/a/div/h4/text()")
date_path = html.xpath("//article/a/div/div/div[@class = 'view-time-box']/text()")

for i in range(len(path)):
    print(title_path[i],'\n',date_path[i].strip(), '\n', path[i])
    print()