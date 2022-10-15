# Notes
'''with open('text.txt', 'w') as f:
    f.write('aaa')
    f.write('\n')

with open('text.txt', 'a') as f:
    f.write('bbb')'''

import requests
from bs4 import BeautifulSoup

html = requests.get('https://www.leagueoflegends.com/en-us/champions/?_gl=1*172i6hr*_ga*Njg4OTkyMTQ5LjE2MDk0ODA5NjE.*_ga_FXBJE5DEDD*MTY0MDY3MTEzMS4xLjAuMTY0MDY3MTEzMS4w').text
soup = BeautifulSoup(html,'html.parser')
hero_div = soup.find('div', class_ = 'style__List-sc-13btjky-2 dLJiol')
a_list = hero_div.find_all('a')

for i in a_list:
    hero_url = 'https://www.leagueoflegends.com' + i['href']
    hero_html = requests.get(url = hero_url).text
    hero_soup = BeautifulSoup(hero_html, 'html.parser')
    hero_img_url = hero_soup.find('div', class_ = 'style__ForegroundAsset-sc-8gkpub-4 fyyYJz')
    hero_img = hero_img_url.find('img')['src']
    hero_name = hero_img.split('/')[-1]
    print('Crawling: ' + hero_name)
    with open('/Volumes/JOEYQIAO/School Mac/Python/1v1/Lesson3/LOL_HEROS/' + hero_name, 'wb') as f:
        f.write(requests.get(hero_img).content)
print('Done')