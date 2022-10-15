#倒入模块
import pgzrun
import random

#一个方块是15*15 长有20个小方块，高有15个
#必须得用WIDTH和HEIGHT因为是pgzrun自带的
#创建窗口
#WIDTH是左右的长度
WIDTH = 15 * 20
#HEIGHT是上下的长度
HEIGHT = 15 * 15

#x轴上有20个方块
grid_x_count = 20
#y轴上有15个方块
grid_y_count = 15

#定义蛇的初始位置（占用3个方块）
#从头开始所以是2，1，0 
#y是0因为在最顶个格
snake = [
    {'x' : 2, 'y' : 0},
    {'x' : 1, 'y' : 0},
    {'x' : 0, 'y' : 0},
]

#定义蛇的随机x,y坐标
food = {
    'x' : random.randint(0, grid_x_count - 1),
    'y' : random.randint(0, grid_y_count - 1)
}

#定义一开始是往右走的
direction = 'right'

#定义时间
timer = 0

#定义蛇是活着的
snake_status = True

#定义draw函数，画出东西
def draw():

    #定义单个方块的大小
    cell_size = 15

    #画出窗口
    #左边的两个数是坐标，右边的两个是大小
    #RGB在pgzun里面是反过来的（0，0，0是黑色）（255，255，255是白色）
    screen.draw.filled_rect(
        Rect(0, 0, WIDTH, HEIGHT),
        color = (70, 70, 70)
    )

    #画出苹果
    #要跟蛇的写法一样，这样才能对上
    screen.draw.filled_rect(
        Rect(food['x'] * cell_size, food['y'] * cell_size, cell_size - 1, cell_size - 1),
        color = (255, 0, 0)
    )

    #循环snake
    for s in snake:
        #画出蛇
        #s['x'] * cell_size 是为了让每次的x乘以15(cell_size)定义它的坐标
        #cell_size - 1 是为了让蛇的身体的每个方块中间有空隙
        #color = (165, 255, 81) 这几个数字让他成一个淡绿色
        screen.draw.filled_rect(
            Rect(
                s['x'] * cell_size, s['y'] * cell_size, 
                cell_size - 1, cell_size - 1
            ),
            color = (165, 255, 81)
        )

#定义update函数让画面动起来
#dt是每次运行的时间
def update(dt):

    #让timer能在update里使用
    global timer, food, snake_status

    #看运行多少次能加到0.1秒
    timer += dt

    #让蛇动，在前面添加一个，然后删掉后面的
    #看如果时间大于0.1就让他停一下再动
    if timer >= 0.1:

        #让头往前走
        #定义蛇的下一个位置
        next_x_position = snake[0]['x']
        next_y_position = snake[0]['y']

        #判断方向，然后往哪个方向走
        #判断如果出了屏幕再从另外一边回来
        if direction == 'right':
            next_x_position += 1

            if next_x_position >= grid_x_count:
                next_x_position = 0

        elif direction == 'left':
            next_x_position -= 1

            if next_x_position < 0:
                next_x_position = grid_x_count - 1

        elif direction == 'up':
            next_y_position -= 1

            if next_y_position < 0:
                next_y_position = grid_y_count - 1

        elif direction == 'down':
            next_y_position += 1

            if next_y_position >= grid_y_count:
                next_y_position = 0


        #判断如果蛇撞到自己了就死了
        for s in snake[:-1]:
            if next_x_position == s['x'] and next_y_position == s['y']:
                snake_status = False

        #判断如果设还活着，在蛇的头前面添加一个方块
        if snake_status:
            snake.insert(0,{'x' : next_x_position, 'y' : next_y_position})
            #如果蛇吃到了苹果这次就不pop掉后面，然后重新随机一下苹果的坐标
            if next_x_position == food['x'] and next_y_position == food['y']:
                food = {
                            'x' : random.randint(0, grid_x_count - 1),
                            'y' : random.randint(0, grid_y_count - 1)
                        }  

            #如果蛇没有迟吃到苹果，就把把后面的删掉
            else:
                snake.pop()

        #把计时器归零等一下，不然就动的太快了
        timer = 0

#定义on_key_down函数监听键盘
def on_key_down(key):

    #让direction能在update里使用
    global direction

    #判断键盘的上下左右来让蛇按照我们的意图来移动
    #不能在蛇往右走的时候突然往左走所以要加一层判断
    if key == keys.RIGHT and direction != 'left':
        direction = 'right'
    if key == keys.LEFT and direction != 'right':
        direction = 'left'
    if key == keys.UP and direction != 'down':
        direction = 'up'
    if key == keys.DOWN and direction != 'up':
        direction = 'down'

#运行程序
pgzrun.go()

#作者：乔一