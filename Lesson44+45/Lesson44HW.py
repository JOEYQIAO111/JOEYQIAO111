import pgzrun

WIDTH, HEIGHT = 800, 600
direction = 'right'
x, y = 0, 0


def draw():
    screen.draw.filled_rect(
        Rect(x, y, 50, 50),
        color=(155, 255, 90)
    )


def on_key_down(key):
    global direction
    if key == keys.LEFT:
        direction = 'left'
    if key == keys.RIGHT:
        direction = 'right'
    if key == keys.UP:
        direction = 'up'
    if key == keys.DOWN:
        direction = 'down'


def update():
    global x,y
    if direction == 'left':
        x -= 2
    if direction == 'right':
        x += 2
    if direction == 'up':
        y -= 2
    if direction == 'down':
        y += 2
    screen.clear()


pgzrun.go()
