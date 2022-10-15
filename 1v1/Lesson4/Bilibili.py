import requests
import json
from bs4 import BeautifulSoup


url = input('Copy and paste the bilibili video url: ')
title_select = input('Do u want to use the original title of the video? (1 : yes, 2 : no): ')

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36',
            'Referer': 'https://www.bilibili.com/'}

if title_select == '1':
    html = requests.get(url).text
    soup = BeautifulSoup(html,'html.parser')
    video_title = soup.find('span', class_ = 'tit').text
else:
    video_title = input('Enter the title u want: ')

BV0 = url.split('?')[0]
BV1 = BV0.split('/')[-1]
if not BV1:
    BV1 = BV0.split('/')[-2]

print('————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————')
print(f'Crawling: {video_title}.mp4')
print('————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————')

api = json.loads(requests.get(f'https://api.bilibili.com/x/player/pagelist?bvid={BV1}&jsonp=jsonp').text)
cid = api['data'][0]['cid']

video_url = json.loads(requests.get(f'https://api.bilibili.com/x/player/playurl?bvid={BV1}&cid={cid}&qn=64').text)

video = video_url['data']['durl'][0]['url']
video1 = requests.get(video, headers = headers)
open(f'/Users/yi.qiao/Desktop/{video_title}.mp4', 'wb').write(video1.content)

print('Done')
print('————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————')