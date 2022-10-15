import easygui as g

#g.msgbox(msg = 'hi', title = 'hi', ok_button = 'hi')

'''if g.ccbox('Girl or Boy', choices = ('Boy', 'Girl')):
    g.msgbox('ok')

else: 
    g.msgbox('ok')'''

'''content = g.textbox(msg = 'hi', title = 'Hi', text = 'blah')
print(content)'''

user_info = g.multpasswordbox('Enter username and password: ', 'Loginyi.', ('Username', 'Passoword'))
print(user_info)