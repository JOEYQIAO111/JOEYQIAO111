import requests as r
import easygui as g

city_code = {
    '北京市': '101010100',
    '海淀区': '101010200',
    '朝阳区': '101010300',
    '顺义区': '101010400',
    '丰台区': '101010900',
    '大兴区': '101011100'
}



city = g.choicebox(msg = '选择地区: ', title = '盗版天气网', choices = (list(city_code.keys())))
code = city_code[city]
headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.109 Safari/537.36 OPR/84.0.4316.43'
    }
response = r.get(f'http://api.help.bj.cn/apis/weather/?id={code}', headers = headers)
data = response.json()
fields = ['城市', '日期', '气温', '风力', '风向', '天气']
values = [data['city'], data['today'], data['temp'], data['wdforce'], data['wd'], data['weather']]
g.multenterbox('', title='盗版天气网',fields=(fields), values=(values))