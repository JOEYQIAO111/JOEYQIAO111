import requests
from bs4 import BeautifulSoup

hero_url = 'https://www.leagueoflegends.com/en-us/champions/akali/'
hero_html = requests.get(url = hero_url).text
hero_soup = BeautifulSoup(hero_html, 'html.parser')
hero_img_url = hero_soup.find('div', class_ = 'style__ForegroundAsset-sc-8gkpub-4 fyyYJz')
hero_img = hero_img_url.find('img')['src']

with open('akali.png', 'wb') as f:
    f.write(requests.get(hero_img).content)