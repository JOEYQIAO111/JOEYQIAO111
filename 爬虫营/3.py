import requests,json
from bs4 import BeautifulSoup

bv = 'BV1xK411G7eF'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36',
            'Referer': 'https://www.bilibili.com/'}

'''url = f'https://api.bilibili.com/x/web-interface/view?bvid={bv}'

r = requests.get(url,headers = headers)
r.encoding = r.apparent_encoding
json_str = json.dumps(r.json(), ensure_ascii = False, indent = 4)
open('video_info.json', 'w', encoding = 'utf-8').write(json_str)

f = open('video_info.json', encoding = 'utf-8')
info = json.load(f)

url = f"https://api.bilibili.com/x/player/pagelist?bvid={bv}&jsonp=jsonp"

r = requests.get(url,headers = headers)
r.encoding = r.apparent_encoding

json_str = json.dumps(r.json(), ensure_ascii = False, indent = 4)
open('video_info.json', 'w', encoding = 'utf-8').write(json_str)

f = open('video_info.json', encoding = 'utf-8')
info = json.load(f)'''

cid = 467586220
'''url = f'https://comment.bilibili.com/{cid}.xml'
r = requests.get(url,headers = headers)
r.encoding = r.apparent_encoding

open('comment.txt','w', encoding = 'utf-8').write(r.text)

soup = BeautifulSoup(r.text)
comments_d = soup.find_all('d')
comments = []
attrs= []
for d in comments_d:
    comments.append(d.text)
    attrs.append(d.attrs['p'])

open('弹幕.txt','w',encoding = 'utf-8').write('\n'.join(comments))'''

url = f'https://api.bilibili.com/x/player/playurl?bvid={bv}&cid={cid}&qn=64'

r = requests.get(url,headers = headers)
r.encoding = r.apparent_encoding

json_str = json.dumps(r.json(), ensure_ascii = False, indent = 4)
open('video_url.json', 'w', encoding = 'utf-8').write(json_str)

f = open('video_url.json', encoding = 'utf-8')
info = json.load(f)

vurl = info['data']['durl'][0]['url']
vr = requests.get(vurl,headers = headers)
open('杰哥不要.mp4','ab').write(vr.content)