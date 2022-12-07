import copy

import pgzrun
import random
from pgzero.actor import Actor

TITLE = 'Studio365'
TILE = 50
WIDTH, HEIGHT = TILE * 10, TILE * 11

star = []
stars = []
score = 0

for i in range(10):
    rows = []
    for u in range(10):
        a = random.randint(1, 5)
        rows.append(a)
    star.append(rows)


def tile_update():
    """
    更新方块位置
    """
    for row in range(10):
        for colum in range(10):
            astar = Actor(f'star{star[row][colum]}')
            astar.top = 50 * row
            astar.left = 50 * colum
            stars.append(astar)


tile_update()


def draw():
    screen.clear()
    for o in stars:
        o.draw()

    screen.draw.text(
        f'score = {score}',
        (180, 510),
        fontsize=40,
        color='white'
    )


def down():
    for j in range(10):
        temp_list = []
        for q in range(10):
            temp_list.append(star[q][j])
        count = 0
        while 0 in temp_list:
            temp_list.remove(0)
            count += 1
        for e in range(count):
            temp_list.insert(0, 0)
        for r in range(10):
            star[r][j] = temp_list[r]


def slide():
    color_id = -1
    for x in range(10):
        temp_list = []
        for v in range(10):
            temp_list.append(star[v][x])
        if sum(temp_list) == 0:
            color_id = x
            break
    print(color_id)
    if color_id != -1:
        for b in range(color_id, 9):
            for m in range(10):
                star[m][b] = star[m][b + 1]
        for v in range(10):
            star[v][9] = 0


def on_mouse_down(pos, button):
    global score
    row_click = pos[1] // TILE
    colum_click = pos[0] // TILE
    connect_set = {(row_click, colum_click)}
    for w in range(20):
        temp_set = copy.deepcopy(connect_set)
        for each in temp_set:
            row = each[0]
            colum = each[1]
            color_id = star[row][colum]
            if row > 0 and star[row - 1][colum] == color_id:
                connect_set.add((row - 1, colum))
            if row < 9 and star[row + 1][colum] == color_id:
                connect_set.add((row + 1, colum))
            if colum > 0 and star[row][colum - 1] == color_id:
                connect_set.add((row, colum - 1))
            if colum < 9 and star[row][colum + 1] == color_id:
                connect_set.add((row, colum + 1))
        temp_set.clear()
    if len(connect_set) >= 2:
        for z, n in connect_set:
            star[z][n] = 0
            score += 1

    down()
    slide()
    tile_update()


def update():
    pass


pgzrun.go()
