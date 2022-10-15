'''import turtle as t

str1 = '永和九年岁在癸丑暮春之初会于会稽山阴之兰亭修禊事也群贤毕至少长咸集此地有崇山峻岭茂林修竹又有清流激湍映带左右引以为流觞曲水列坐其次虽无丝竹管弦之盛一觞一咏亦足以畅叙幽情是日也天朗气清惠风和畅仰观宇宙之大俯察品类之盛所以游目骋怀足以极视听之娱信可乐也夫人之相与俯仰一世或取诸怀抱悟言一室之内或因寄所托放浪形骸之外虽趣舍万殊静躁不同当其欣于所遇暂得于己快然自足不知老之将至及其所之既倦情随事迁感慨系之矣向之所欣俯仰之间已为陈迹犹不能不以之兴怀况修短随化终期于尽古人云死生亦大矣岂不痛哉每览昔人兴感之由若合一契未尝不临文嗟悼不能喻之于怀固知一死生为虚诞齐彭殇为妄作后之视今亦犹今之视昔悲夫故列叙时人录其所述虽世殊事异所以兴怀其致一也后之览者亦将有感于斯文'
result = []

for i in range(0, len(str1), 12):
    result.append(str1[i:i+12])

t.setup(1300, 500)
t.bgpic('bg.gif')
t.hideturtle()
t.speed(0)
t.up()

x, y = 400, 175
first = result[0]

for u in result:
    for i in u:
        t.goto(x, y)
        t.write(i, font = ('王羲之书法字体', 25, 'normal'))
        y -= 35
    x -= 40
    y = 175

t.done()'''

'''import turtle as t
import time

t.speed(0)
t.hideturtle()

def draw():
    for i in range(4):
        t.fillcolor('green')
        t.begin_fill()
        t.fd(100)
        t.left(150)
        t.fd(70)
        t.end_fill()
        t.fillcolor('yellow')
        t.begin_fill()
        t.left(30)
        t.fd(40)
        t.left(90)
        t.fd(35)
        t.end_fill()

draw()

for i in range(100000000000000000000000000000000000000000000000000000000000000000):
    t.clear()
    t.tracer(False)
    t.setheading(i * 2)
    draw()
    time.sleep(0.01)
    t.update()

t.done()'''

num = 0
nums = []
while num < 1001:
    num += 1
    if num % 2 == 0:
        nums.append(num)
print(sum(nums))