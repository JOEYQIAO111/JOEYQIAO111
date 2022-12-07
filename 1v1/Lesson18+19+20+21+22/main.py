import pgzrun
import random
from pgzero.keyboard import keyboard, keys
from pgzero.loaders import sounds
from pgzhelper import Actor

# 定义窗口名称
TITLE = 'Studio365'

# 定义窗口大小
WIDTH = 480
HEIGHT = 670

# 定义飞机
plane = Actor('me1', (240, 600))
plane.scale = 0.7
plane.double = False
plane.auto = False
stop = False
bomb = Actor('bomb', (440, 30))
# 定义背景图
bg = Actor('background')
score = 0

sounds.game_music.play()

# 定义储存子弹的列表
bullets = []
# 定义储存外星人的列表
aliens = []
# 定义储存中型外星人的列表
enemy2s = []
# 定义储存心的列表
hearts = []
bombs = []
bullets_supply = []
time = 0
bullet_time = 0.15

mute = False

# 添加生命值
for i in range(5):
    heart = Actor('heart', (20 + 45 * i, 650))
    hearts.append(heart)

# 定义飞机的移动速度
plane.speed = 7

# 定义等级
level = 1
bomb.count = 1


def levels():
    global level

    if 20 <= score < 40:
        level = 2

    elif 40 <= score < 60:
        level = 3

    elif 60 <= score < 80:
        level = 4


# 画出图像
def draw():
    global stop
    bg.draw()

    if hearts:
        bomb.draw()
        screen.draw.text(
            f'{bomb.count}',
            color='red',
            fontsize=50,
            midtop=(440, 60)
        )
        plane.image = f'me{random.randint(1, 2)}'
        plane.draw()
        for i in bullets:
            i.draw()
        for u in aliens:
            u.draw()
        for o in hearts:
            o.draw()
        for i in enemy2s:
            i.draw()
        for i in bombs:
            i.draw()
        for w in bullets_supply:
            w.draw()

    if not hearts:
        stop = True
        screen.draw.text(
            'YOU DIED',
            color='red',
            fontsize=120,
            midtop=(WIDTH // 2, 300)
        )
        screen.draw.text(
            'Click R to restart',
            color='black',
            fontsize=50,
            midtop=(WIDTH // 2, 400)
        )
        sounds.game_music.stop()

    screen.draw.text(
        'M to mute',
        color='black',
        fontsize=20,
        midtop=(440, 650)
    )

    screen.draw.text(
        f'Score:{score}',
        (0, 0),
        color='black',
        fontsize=50,
    )

    if stop and hearts:
        screen.draw.text(
            'Paused',
            fontsize=100,
            color='black',
            midtop=(WIDTH / 2, HEIGHT / 2)
        )


# 让飞机监测键盘然后前后左右移动
def player_move():
    # 点wasd
    if keyboard.w and plane.y > 35:
        plane.y -= plane.speed
    if keyboard.a and plane.x > 20:
        plane.x -= plane.speed
    if keyboard.s and plane.y < 650:
        plane.y += plane.speed
    if keyboard.d and plane.x < 460:
        plane.x += plane.speed

        # 点方向键
    if keyboard.up and plane.y > 35:
        plane.y -= plane.speed
    if keyboard.left and plane.x > 20:
        plane.x -= plane.speed
    if keyboard.down and plane.y < 650:
        plane.y += plane.speed
    if keyboard.right and plane.x < 460:
        plane.x += plane.speed


# 让子弹移动
def bullet_move():
    for i in bullets:
        i.y -= i.speed
        if i.y < 0:
            bullets.remove(i)


def alien():
    global score

    if len(aliens) < 2 * level:
        alien = Actor('enemy1', (random.randint(0, WIDTH), random.randint(-400, 0)))
        alien.speed = 4
        aliens.append(alien)

    for u in aliens:
        u.y += u.speed
        for e in bullets:
            if crash(u, e):
                try:
                    aliens.remove(u)
                    bullets.remove(e)
                except:
                    pass
                score += 1
                if not mute:
                    sounds.enemy1_down.play()

        if u.y >= HEIGHT:
            aliens.remove(u)

    for p in aliens:
        if crash(p, plane) and hearts:
            del hearts[-1]
            aliens.remove(p)
            if not mute:
                sounds.enemy1_down.play()
                sounds.me_down.play()
            plane.pos = 240, 600


def alien1():
    global score
    if level >= 2:
        if len(enemy2s) < level:
            enemy2 = Actor('enemy2', (random.randint(0, WIDTH), random.randint(-400, 0)))
            enemy2.speed = 3
            enemy2.health = 5
            enemy2s.append(enemy2)

    for i in enemy2s:
        i.y += i.speed
        if i.health == 0:
            enemy2s.remove(i)
            score += 3
            if not mute:
                sounds.enemy2_down.play()
            break
        for e in bullets:
            if crash(i, e):
                i.health -= 1
                bullets.remove(e)

        if i.y >= HEIGHT:
            enemy2s.remove(i)

    for p in enemy2s:
        if crash(p, plane) and hearts:
            del hearts[-1]
            enemy2s.remove(p)
            if not mute:
                sounds.enemy2_down.play()
                sounds.me_down.play()
            plane.pos = 240, 600


def shoot_bullet():
    if not plane.double:
        bullet = Actor('bullet', (plane.x, plane.y))
        bullet.speed = 12
        bullets.append(bullet)
    else:
        bullet = Actor('bullet', (plane.x - 20, plane.y))
        bullet.speed = 12
        bullet1 = Actor('bullet', (plane.x + 20, plane.y))
        bullet1.speed = 12
        bullets.append(bullet)
        bullets.append(bullet1)


t = 0


def auto_bullet(dt):
    global t
    t += dt
    if t > bullet_time:
        shoot_bullet()
        t = 0


def crash(actor1, actor2):
    if actor1.collide_pixel(actor2):
        return True
    return False


# 发射子弹
def on_key_down(key):
    global mute, stop
    if not stop:
        if key == keys.SPACE or key == keys.RSHIFT or key == keys.J and not plane.auto:
            shoot_bullet()
            if not mute:
                sounds.bullet.play()

    if not hearts and key == keys.R:
        restart()

    if key == keys.M:
        mute = not mute
        if not mute:
            sounds.game_music.play()
        else:
            sounds.game_music.stop()

    if key == keys.ESCAPE:
        stop = not stop

    if key == keys.B and bomb.count >= 1:
        use_bomb()

    if key == keys.T:
        plane.auto = not plane.auto


def use_bomb():
    global score, aliens, enemy2s
    score += (len(aliens) + len(enemy2s) * 3)
    bomb.count -= 1
    aliens = []
    enemy2s = []
    if not mute:
        sounds.use_bomb.play()


def get_bomb():
    if random.randint(0, 400) == 1 and bombs == [] and level > 2 and bomb.count < 5:
        bomb_supply = Actor('bomb_supply', (random.randint(0, 480), -10))
        bombs.append(bomb_supply)

    for i in bombs:
        i.y += 4
        if crash(i, plane):
            if not mute:
                sounds.get_bomb.play()
            bomb.count += 1
            bombs.remove(i)


def get_bullet():
    if random.randint(0, 400) == 1 and bullets_supply == [] and level > 2 and not plane.double:
        bullet_supply = Actor('bullet_supply', (random.randint(0, 480), -10))
        bullets_supply.append(bullet_supply)

    for p in bullets_supply:
        p.y += 4
        if crash(p, plane):
            if not mute:
                sounds.get_bullet.play()
            plane.double = True
            bullets_supply.remove(p)


def remove_bullet(dt):
    global time
    if plane.double:
        time += dt
        if time > 6:
            plane.double = False
            time = 0


def restart():
    global score, level, aliens, enemy2s, stop
    for i in range(5):
        heart = Actor('heart', (20 + 45 * i, 650))
        hearts.append(heart)
        score = 0
        level = 1
        bomb.count = 1
        aliens = []
        enemy2s = []
        stop = False
    if not mute:
        sounds.game_music.play()


# 更新画面
def update(dt):
    if not stop:
        player_move()
        bullet_move()
        alien()
        alien1()
        levels()
        get_bomb()
        get_bullet()
        remove_bullet(dt)
        if plane.auto:
            auto_bullet(dt)

# 运行程序
pgzrun.go()
