# 通过接口筛选数据
import requests
import json

def get_video(title, bvid, cid):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36',
            'Referer': 'https://www.bilibili.com/'}
    video_info = json.loads(requests.get(f"https://api.bilibili.com/x/player/playurl?bvid={bvid}&cid={cid}&qn=64").text)
    vurl = video_info['data']['durl'][0]['url']
    vr = requests.get(vurl,headers=headers)
    open(f'{title}.mp4','ab').write(vr.content) 


# 拿到接口数据
bi_data = json.loads(requests.get('https://api.bilibili.com/x/web-interface/popular?ps=20&pn=1').text)
data = bi_data['data']['list']
title = []
bvid = []
cid = []
for i in data:
    title.append(i['title'])
    bvid.append(i['bvid'])
    cid.append(i['cid'])

for u in range(len(title)):
    print(f'Crawling 《{title[u]}》')
    get_video(title[u], bvid[u], cid[u])
print('finished crawling')