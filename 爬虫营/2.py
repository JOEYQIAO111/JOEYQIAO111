import os
import re
import requests
from bs4 import BeautifulSoup

def get_html(url,html_name):
    r = requests.get(url,timeout = 10)
    r.encoding = r.apparent_encoding
    #open(f'{html_name}.txt','w',encoding = 'utf-8').write(r.text)
    return r.text

def save_picture(link,name,_id):     
    url = 'https://pvp.qq.com/web201605/' + link
    html = get_html(url,name + 'skin')
    soup = BeautifulSoup(html,'html.parser')
    print(f'正在获取{name}的皮肤链接')
    skin_name = soup.select('.pic-pf ul')[0].attrs['data-imgname']
    count = skin_name.count('&')
    skin_name = skin_name.replace('&','')
    for i in range(10):
        skin_name = skin_name.replace(str(i), '')
    skin_list = skin_name.split('|')
    local_path = './/王者荣耀英雄皮肤//' + name + '\\'
    if not os.path.exists(local_path):
        os.mkdir(local_path)
    base_pic_link = 'https://game.gtimg.cn/images/yxzj/img201606/heroimg/'
    for i in range(1, count + 1):
        pic = f'{_id}/{_id}-smallskin-{i}.jpg'
        pic_url = base_pic_link + pic
        pic_html = requests.get(pic_url, timeout = 10)
        f = open(local_path + skin_list[i-1] + '.jpg', 'wb')
        f.write(pic_html.content)

def get_link(html):
    print('正在查找所有英雄链接....')
    soup = BeautifulSoup(html,'html.parser')
    herolist = soup.find_all('a',href = re.compile('herodetail'))
    for each in herolist:
        link = each.attrs['href']
        name = each.select('img')[0].attrs['alt']
        _id = link[11:14]
        save_picture(link,name,_id)

url = 'https://pvp.qq.com/web201605/herolist.shtml'
html = get_html(url,'data')
get_link(html)