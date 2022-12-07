import pgzrun
from pgzhelper import Actor

WIDTH, HEIGHT = 1250, 300
bg = Actor('background', (640, 0))
me = Actor('me', (40, 145))
zombie = Actor('zombie', (1260, 160))
me.jump = False
me.fall = False
me.die = False
step = 1


def draw():
    bg.draw()
    if step % 2 != 0:
        me.image = 'me1'
    if step % 2 == 0:
        me.image = 'me2'
    if me.jump:
        me.image = 'jump'
    if me.die:
        screen.draw.text(
            'YOU DIED',
            midtop=(WIDTH/2, 70),
            color='red',
            fontsize=300
        )

    zombie.draw()
    me.draw()


def on_key_down(key):
    if not me.die:
        global step

        if key == keys.LEFT:
            me.x -= 10
            step += 1
            sounds.move.play()

        elif key == keys.RIGHT:
            me.x += 10
            step += 1
            sounds.move.play()

        elif key == keys.UP and me.y == 145:
            me.jump = 5


def zombies():
    zombie.x -= 7
    if zombie.x < 20:
        zombie.x = 1460


def jump():
    me.y -= 2 * me.jump
    if me.y < 145:
        me.jump -= 0.2
    else:
        me.y = 145
        me.jump = 0


def collide():
    if me.colliderect(zombie):
        me.die = True


def update():
    if not me.die:
        jump()
        zombies()
        collide()


pgzrun.go()
