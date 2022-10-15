import requests
from bs4 import BeautifulSoup

for e in range(1,10):
    html = requests.get(f'https://quotes.toscrape.com/page/{e}/')
    soup = BeautifulSoup(html.text, "html.parser")

    tag_list = soup.find_all('span', itemprop = 'text')
    tag_list_author = soup.find_all('small', itemprop = 'author')
    for i in range(len(tag_list)):
        with open(f'/Volumes/JOEYQIAO/School Mac/Python/1v1/Lesson1/Quotes.txt', 'a') as f:
            f.write(tag_list[i].string)
            f.write('\n')
            f.write(f'Author: {tag_list_author[i].string}\n')
            f.write('\n')
    print(f'Page{e} has been crawled')