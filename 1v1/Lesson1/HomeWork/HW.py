import requests
from bs4 import BeautifulSoup

html = requests.get('http://book.zongheng.com/showchapter/1169984.html')
soup = BeautifulSoup(html.text, "html.parser")
title = soup.find_all('li', class_="col-4")

for i in range(2,80):
    link = title[i].contents[1]['href']
    html = requests.get(link)
    soup = BeautifulSoup(html.text, "html.parser")
    content = soup.find_all('p')
    chapter = soup.find('div', class_ = 'title_txtbox')
    with open(f'/Volumes/JOEYQIAO/School Mac/Python/1v1/Lesson1/HomeWork/星际生存从侵略开始_前十章.txt', 'a') as f:
        f.write('\n')
        f.write(chapter.string)
        for tag in content[:-1]: 
            f.write('\n')
            f.write(tag.string)

    print(f'Chapter{i-1} has been crawled')