import turtle
import random

turtle.setup(600,400)
turtle.hideturtle()
turtle.listen()
turtle.up()
turtle.goto(100,150)
turtle.tracer(False)
gifs = ['bird1', 'bird2', 'cactus', 'dino_down1', 'dino_down2', 'dino1', 'dino2', 'dino3', 'dino4', 'ground' ]

for gif in gifs:
    turtle.addshape('C:\Users\filth\Documents\Python\dino\dino1.gif\\' + gif + '.gif')

g = [600,0]
di = [-200,25]
b = [210,20]
cacti = {}

def tap():
    if state['jump'] == 0  or state['n'] < 3:
        state['jump'] = 2
        state['n'] += 1

def jump():
    di[1] += 16 * state['jump']
    
    if di[1] > 25:
        state['jump'] -=0.4
    else:
        state['jump'] =  0
        state['n'] = 0
        di[1] = 25

def down():
    state['down'] = 1

def up():
    state['down'] = 0

def draw(alive):
    turtle.clear()
    state['count'] += 1
    ground.goto(g)
    bird.shape('D:\PC\Python\dino\\bird' + str(state['count'] % 2 + 1) + '.gif')
    bird.goto(b[0], b[1])
    
    state['score'] += 1
    turtle.write('Score: ' + str(state['score']), font = ('',30, ''))

    if alive == True:
        if state['down'] == 0:
            dino1.shape('D:\PC\Python\dino\\dino' + str(state['count'] % 3 + 1) + '.gif')
        else:
            dino1.shape('D:\PC\Python\dino\\dino_down' + str(state['count'] % 2 + 1) + '.gif')

    else:
        dino1.shape('D:\PC\Python\dino\\dino4.gif')

    dino1.goto(di)
    
    if random.randint(1,10) == 1:
        cactus = turtle.Turtle()
        cactus.shape('D:\PC\Python\dino\\cactus.gif')
        cactus.up()
        cacti[cactus] = 300
    
    for cactus, x in cacti.items():
        cactus.goto(x,25)
    
    turtle.update()

def move():
    jump()

    for cactus in cacti.keys():
        if abs(di[0] - cacti[cactus]) <= 20 and abs(di[1] - 15) <= 35:
            draw(False)
            return False

    if abs(di[0] - b[0]) <= 25 and abs(di[1] - b[1]) <= 20:
        draw(False)
        return False

    g[0] = g[0] - 15
    if g[0] == -600:
        g[0] = 600

    b[0] -= 25
    if b[0] <= -310:
        b[0] = 310
        b[1] = random.randint(20,80)

    if di[1] >= 25:
        di[1] -= 5
    else:
        state['jump'] = 0 

    for cactus in cacti.keys():
        cacti[cactus] -= 15   

    draw(True)
    turtle.ontimer(move,50)

ground = turtle.Turtle() 
ground.shape('D:\PC\Python\dino\\ground.gif')
ground.up()

dino1 = turtle.Turtle()
dino1.shape('D:\PC\Python\dino\\dino1.gif')
dino1.up()
state = {'count' : 0, 'jump' : 0,'n' : 0, 'score' : 0, 'down' : 0}

bird = turtle.Turtle()
bird.shape('D:\PC\Python\dino\\bird1.gif')
bird.up()

turtle.onkeypress(tap, 'space')  
turtle.onkeypress(down, 'Down')
turtle.onkeyrelease(up, 'Down')

move()
turtle.done()