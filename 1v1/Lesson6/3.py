import easygui as g
import requests
user = ['1', '2']
user_info = g.multpasswordbox("请输入用户名和密码", "用户登录接口",("用户名","密码"))
if user_info != user:
    g.msgbox("密码错误")
else:
    content = g.textbox(msg='翻译大全', title='请输入你要翻译的内容', text='')
    base_url = 'https://fanyi.baidu.com/sug'
    data = {
        'kw': content
    }
    headers = {
        'content-length': str(len(data)),
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'referer': 'https://fanyi.baidu.com/',
        'x-requested-with': 'XMLHttpRequest'
    }
    response = requests.post(base_url, headers=headers, data=data)
    #结果：{'errno': 0, 'data': [{'k': 'python', 'v': 'n. 蟒; 蚺蛇;'}, {'k': 'pythons', 'v': 'n. 蟒; 蚺蛇;  python的复数;'}]}
    result=''
    for i in response.json()['data']:
        result+=i['v']+'\n'

    g.textbox(msg='翻译大全', title='翻译结果为', text=result)
