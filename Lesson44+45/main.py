import pgzrun
import random

WIDTH, HEIGHT = 600, 720
TITLE = '盗版养了个杨'
#播放背景音乐
music.play('bgm')
#定义背景图片
bg = Actor('back')
#储存tile Actor 的列表
T_WIDTH = 60
T_HEIGHT = 66

dock = []
tiles = []
#定义储存图片的索引的列表
ts = list(range(1, 13))*12
#打乱列表里的顺序
random.shuffle(ts)
#定义第几块
n = 0

DOCK = Rect((90, 564), (T_WIDTH*7, T_HEIGHT))

#生成tile
#层
for i in range(7):
    #行
    for u in range(7-i):
        #列
        for o in range(7-i):
            #找到每一块tile
            t = ts[n]
            #每次循环都加一
            n += 1
            #定义每个tile的Actor
            tile = Actor(f'tile{t}')
            #定义每块tile的位置
            tile.pos = 120 + (i * 0.5 + o) * tile.width, 100 + (i * 0.5 + u) * tile.height
            #定义它是哪种tile
            tile.tag = t
            #定义它是第几层
            tile.layer = i
            tile.status = 1 if i == 6 else 0
            tiles.append(tile)

#添加生下4块tile
for i in range(4):
    t = ts[n]
    n += 1
    tile = Actor(f'tile{t}')
    tile.pos = 210 + i*5, 516
    tile.tag = t 
    tile.layer = 0
    tile.status = 1
    tiles.append(tile)

def draw():
    #画出背景图片
    bg.draw()

    for tile in tiles:
        tile.draw()
        if tile.status == 0:
            screen.blit('mask', tile.topleft) 

    for i,tile in enumerate(dock):
        tile.left = (DOCK.x + i*T_WIDTH)
        tile.top = DOCK.y
        tile.draw()
    
    for i in dock:
        i.draw()

    if len(dock) > 7:
        screen.blit('end', (0,0))

    if len(tiles) == 0:
        screen.blit('win', (0,0))    


def on_mouse_down(pos):
    global dock
    for tile in reversed(tiles):
        if tile.status == 1 and tile.collidepoint(pos):
            dock.append(tile)
            tiles.remove(tile)

            diff = [i for i in dock if i.tag != tile.tag]
            if len(dock) - len(diff) == 3:
                dock = diff         

            for down in tiles:
                if down.layer == tile.layer-1 and down.colliderect(tile):
                    for up in tiles:
                        if up.layer == down.layer+1 and up.colliderect(down):
                            break
                    else:
                        down.status = 1
            break

def update():
    pass

pgzrun.go()