#sg.popup('中间现实的东西', title = '提示‘)
#sg.popup_ok_cancel('Done', title = '提示')

import PySimpleGUI as sg
a = sg.popup_ok_cancel('Done', title = '提示')
print(a)