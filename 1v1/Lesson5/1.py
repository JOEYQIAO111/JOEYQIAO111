# pip3 install lxml
from lxml import etree
wb_data = """
        <div>
            <ul>
                 <li class="item-0"><a href="link1.html">first item</a></li>
                 <li class="item-1"><a href="link2.html">second item</a></li>
                 <li class="item-inactive"><a href="link3.html">third item</a></li>
                 <li class="item-1"><a href="link4.html">fourth item</a></li>
                 <li class="item-0"><a href="link5.html">fifth item</a>
             </ul>
         </div>
        """
html = etree.HTML(wb_data)

# 查找所有li标签下的a
'''a0 = html.xpath('/html/body/div/ul/li/a')
for i in a0:
    print(i.text)'''
# 获取某个标签的内容
'''a1 = html.xpath('//a')
for i in a1:
    print(i.text)'''
# 打印指定路径下a标签的属性
'''a2 = html.xpath('//a/text()')
print(a2)

a3 = html.xpath('//a/@href')
print(a3)'''
# 相对路径//
'''a4 = html.xpath("//li[@class = 'item-0']/a/@href")
print(a4)'''
# 查特定属性 [@xxx=" "]

a5 = html.xpath("//li/a[@href = 'link2.html']/text()")
print(a5)