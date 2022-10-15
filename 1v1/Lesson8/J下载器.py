import PySimpleGUI as sg
import requests
import json

username = 'Jadmin'
password = '1234qwer'

login_window = [
    [sg.T('Username: ')],
    [sg.In(key = 'username')],
    [sg.T('Password: ')],
    [sg.In(password_char = '*', key = 'password')],
    [sg.Exit('Cancel'), sg.Button('Ok')]
]

login_Window = sg.Window('J下载器', login_window)
event, values = login_Window.read()
login_Window.close()

if values['username'] == username and values['password'] == password:
    while True:
        window = [
            [sg.Text('视频地址:')],
            [sg.Input(key='url')],
            [sg.Text('保存地址:')],
            [sg.In(key='path'), sg.FolderBrowse(target='path')],
            [sg.Text('下载几集:')], 
            [sg.Slider(range=(1,50),orientation='horizontal', key='num')],
            [sg.Exit('取消'), sg.Button('确认')]
        ]
        Window = sg.Window('J下载器', window)
        event, values = Window.read()

        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36',
                'Referer': 'https://www.bilibili.com/'}
        
        url = values['url']
        path = values['path']
        num = int(values['num'])

        BV0 = url.split('?')[0]
        BV1 = BV0.split('/')[-1]
        if not BV1:
            BV1 = BV0.split('/')[-2]
        
        for i in range(num):
            api = json.loads(requests.get(f'https://api.bilibili.com/x/player/pagelist?bvid={BV1}&jsonp=jsonp').text)
            cid = api['data'][i]['cid']

            video_url = json.loads(requests.get(f'https://api.bilibili.com/x/player/playurl?bvid={BV1}&cid={cid}&qn=64').text)

            video = video_url['data']['durl'][0]['url']
            video1 = requests.get(video, headers = headers)
            open(f'{path}/{i}.mp4', 'wb').write(video1.content)
        a = sg.popup_ok_cancel('下载完成 是否继续下载', title = 'J下载器')
        if a == 'Cancel':
            break
        Window.close()

else:
    while True:
        sg.popup('Wrong password or username!', title = 'HAHAHAHA')