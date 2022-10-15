import requests
import os
from bs4 import BeautifulSoup

html = requests.get('https://www.leagueoflegends.com/en-us/champions/?_gl=1*172i6hr*_ga*Njg4OTkyMTQ5LjE2MDk0ODA5NjE.*_ga_FXBJE5DEDD*MTY0MDY3MTEzMS4xLjAuMTY0MDY3MTEzMS4w').text
soup = BeautifulSoup(html,'html.parser')
hero_div = soup.find('div', class_ = 'style__List-sc-13btjky-2 dLJiol')
a_list = hero_div.find_all('a')

for i in a_list:
    hero_url = 'https://www.leagueoflegends.com' + i['href']
    hero_html = requests.get(url = hero_url).text
    hero_soup = BeautifulSoup(hero_html, 'html.parser')
    hero_img_url = hero_soup.find('div', class_ = 'style__Slideshow-gky2mu-2 jQOWwL')
    hero_img = hero_img_url.find_all('div', class_ = 'style__SlideshowItem-gky2mu-3 gPdDAX')

    count = 0
    for u in hero_img:
        count += 1
        hero_skin_url = u.find('img')['src']
        hero_skin_name = hero_skin_url.split('/')[-1]
        folder_name = hero_skin_name.split('_')[0]
        if count == 1:
            os.mkdir('/Volumes/JOEYQIAO/School Mac/Python/1v1/Lesson3/LOL_HERO_SKINS/' + folder_name)
        print('Crawling: ' + hero_skin_name)

        with open(f'/Volumes/JOEYQIAO/School Mac/Python/1v1/Lesson3/LOL_HERO_SKINS/{folder_name}/' + hero_skin_name, 'wb') as f:
            f.write(requests.get(hero_skin_url).content)
print('Done')