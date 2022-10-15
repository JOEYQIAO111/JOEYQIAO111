from bs4 import BeautifulSoup

html = '''
<html>
 <head>
  <base href='http://example.com/' />
  <title>Example website</title>
 </head>
 <body>
  <div id='images'>
   <a href='image1.html'>Name: My image 1</a>
   <a href='image1.html'>Name: My image 1</a>
   <a href='image2.html'>Name: My image 2</a>
   <a href='image2.html'>Name: My image 2</a>
  </div>
 </body>
</html>
'''

soup = BeautifulSoup(html, 'html.parser')
title = soup.title
tag_list = soup.find_all('a', href = 'image1.html')
'''print(title)
print(title.string)'''
print(tag_list)
for i in tag_list:
    print(i.string)