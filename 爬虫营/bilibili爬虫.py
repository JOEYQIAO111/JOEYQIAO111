import requests,json
from bs4 import BeautifulSoup
from requests.models import CaseInsensitiveDict


def get_url_json(url,filename):
    r = requests.get(url,headers = headers)
    r.encoding = r.apparent_encoding
    #写入json
    json_str = json.dumps(r.json(),ensure_ascii=False,indent=4)
    open(f'{filename}.json','w',encoding='utf-8').write(json_str)
    #读取json
    f = open(f'{filename}.json',encoding='utf-8')
    info = json.load(f)
    return info
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36',
            'Referer': 'https://www.bilibili.com/'}
bv = input('输入BV号：')
video_name = input('创建视频文件名：')
cid_url = f"https://api.bilibili.com/x/player/pagelist?bvid={bv}&jsonp=jsonp"
cid_info = get_url_json(cid_url,'cid_info') 
cid = cid_info['data'][0]['cid']

video_url = f"https://api.bilibili.com/x/player/playurl?bvid={bv}&cid={cid}&qn=64"
video_info = get_url_json(video_url,'video_info')

vurl = video_info['data']['durl'][0]['url']
vr = requests.get(vurl,headers=headers)
open(f'{video_name}.mp4','ab').write(vr.content) 