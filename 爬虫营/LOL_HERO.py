import os
import re
import requests
from bs4 import BeautifulSoup

def get_html(url,html_name):
    headers = {'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 Edg/96.0.1054.62"}
    r = requests.get(url,timeout = 120,headers = headers)
    r.encoding = r.apparent_encoding
    open(f'{html_name}.txt','w',encoding = 'utf-8').write(r.text)
    return r.text

url = 'https://www.leagueoflegends.com/en-us/champions/?_gl=1*172i6hr*_ga*Njg4OTkyMTQ5LjE2MDk0ODA5NjE.*_ga_FXBJE5DEDD*MTY0MDY3MTEzMS4xLjAuMTY0MDY3MTEzMS4w'
html = get_html(url,'LOL_data')

soup = BeautifulSoup(html,'html.parser')
L = soup.find_all('a', href = re.compile('/en-us/champions/'))

img_list = []
name = []

for each in L:
    img_list.append(each.span.img.attrs['src'])
    name.append(each.attrs['herf'].split('/')[-2])

local_path = './/LOL_HERO_PIC//'

for u in range(len(img_list)):
    pic = requests.get(img_list[u])
    open(local_path + f'{name[u]}.jpg','wb').write(pic.content)