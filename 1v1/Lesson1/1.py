#https://quotes.toscrape.com/
import requests
for i in range(1,4):
    res = requests.get(f'https://quotes.toscrape.com/page/{i}/')
    print(f'爬取{i}')

'''requests 的简单使用  https://quotes.toscrape.com/ 
https://api.bilibili.com/x/web-interface/popular?ps=20&pn=1
get(得到数据)  post(发送数据)  put(更新数据)  delete(删除)

status_code  2: 成功
content
text
json()
"""

import requests
for i in range(1,4):
    res = requests.get(f'https://quotes.toscrape.com/page/{i}/')
    print(f"第{i}页已经爬取")'''