import easygui as g
import requests

user_id = ['J','111222']

'''while True:
    user_info = g.multpasswordbox('Enter username and password: ', 'Login', ('Username', 'Passoword'))
    if user_info != user_id:
        if g.ccbox('Wrong passord or username', choices = ('Cancel', 'Retry')):
            continue 
        else:
            break
            break
            break
    if user_info != user_id:
        g.textbox(msg = '盗版百度翻译', title = '盗版百度翻译', text = '输入英语单词: ')'''

while True:
    user_info = g.multpasswordbox('Enter username and password: ', 'Login', ('Username', 'Passoword'))

    if user_info != user_id:
        g.msgbox('Wrong Password or Username')
        
    if user_info == user_id:
        break

word = g.textbox(msg = '输入英语单词: ', title = '盗版百度翻译', text = '')
url = 'https://fanyi.baidu.com/sug'

data = {
    'kw' : word
}

headers = {
    'x-requested-with': 'XMLHttpRequest',
    'referer': 'https://fanyi.baidu.com/',
    'Content-Type' : 'application/x-www-form-urlencoded; charset=UTF-8',
    'Content-Length' : str(len(data))
}

result = ''
response = requests.post(url, headers = headers, data = data)
    
for i in response.json()['data']:
    result += i['k'] + '\n' + i['v'] + '\n'
    
g.textbox(msg = '单词意思： ', title = '盗版百度翻译', text = result)