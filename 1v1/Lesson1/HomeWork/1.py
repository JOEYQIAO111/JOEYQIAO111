import requests
from bs4 import BeautifulSoup
html = requests.get('http://book.zongheng.com/showchapter/1169984.html')
soup = BeautifulSoup(html.text, "html.parser")
# 找到所有章节列表, 格式如下，可以发现有共同属性 class = "col-4"，使用find_all查找
"""
<li class=" col-4">
    <a  href="http://book.zongheng.com/chapter/1169984/67173965.html">第1章 加入星际舰队</a>
</li>                 
<li class=" col-4">
    <a  href="http://book.zongheng.com/chapter/1169984/67173966.html">第2章 初窥木星</a>
</li>
"""
# 因class属性和python冲突，所以为class_
title = soup.find_all('li', class_="col-4")
# 这里你会发现抓取的每个值的结构为  <li> <a></a> </li>，两层结构
# 所以使用了contents[1]为<a></a>标签，['href']为a标签内部的href的值，即每一章的跳转链接
# 至此拿到title列表
for i in title:
    print(i.contents[1].string, '--->', i.contents[1]['href'])