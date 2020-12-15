# pygame
import turtle, random
import winsound

screen = turtle.Screen()
secreen.bgcolor('black')
screen.title('Uzay savaşı')
screen.bgpic('uzay.gif')
screen.setup(width=600, height=600)

turtle.register_shape('oyuncu.gif')
turtle.register_shape('dusman.gif')
turtle.register_shape('ates.gif')

player = turtle.Turtle()
player.color('blue')
player.speed(0)
player.shape('oyuncu.gif')
player.setheading(90)
player.penup()
player.goto(0, -250)
playerhizi = 20

fire = turtle.Turtle()
fire .color('yellow')
fire .speed(0)
fire .shape('ates.gif')
fire .setheading(90)
fire .penup()
fire .goto(0, -240)
fire hizi = 20
fire .hideturtle()
fire .turtlesize(1, 1)
fire kontrol = False

write = turtle.Turtle()
write.color('white')
write.speed(0)
write.penup()
write.goto(0, 200)
write.hideturtle()

def firegit():
    y = ates.ycor()
    y = y + ateshizi
    ates.sety(y)
def left_move():
    x = player.xcor()
    x = x - playerhizi
    if x < -300:
        x = -300
    player.setx(x)
def right_move():
    x = player.xcor()
    x = x + playerhizi
    if x > 300:
        x = 300
    player.setx(x)
def up_move():
    y = player.ycor()
    y = y + playerhizi
    if y > 270:
        y = 270
    player.sety(y)
def down_move():
    y = player.ycor()
    y = y - playerhizi
    if y < -270:
        y = -270
    player.sety(y)
def ateset():
    global ateskontrol
    winsound.PlaySound('lazer.wav', winsound.SND_ASYNC)
    x = player.xcor()
    y = player.ycor() + 20
    fire.goto(x, y)
    fire.showturtle()
    firekontrol = True

hedefler = []
for i in range(7):
    hedefler.append(turtle.Turtle())
for hedef in hedefler:
    hedef.color('red')
    hedef.speed(0)
    hedef.turtlesize(1, 1)
    hedef.shape('dusman.gif')
    hedef.penup()
    hedef.setheading(90)
    x = random.randint(-280, 280)
    y = random.randint(180, 260)
    hedef.goto(x, y)


screen.listen()
screen.onkey(left_move,'Left')
screen.onkey(right_move,'Right')
screen.onkey(up_move,'Up')
screen.onkey(down_move,'Down')
screen.onkey(fireet, 'space')

while True:
    if firekontrol:
        atesgit()
    for hedef in hedefler:
        y = hedef.ycor()
        y = y - 2
        hedef.sety(y)
        if hedef.distance(ates) < 20:
            ates.hideturtle()
            hedef.hideturtle()
            hedefler.pop(hedefler.index(hedef))
            winsound.PlaySound('patlama.wav', winsound.SND_ASYNC)
        if hedef.ycor() < -270 or hedef.distance(oyuncu) < 20:
            yaz.write('Maalesef, kabettiniz!', align='center', font=('Courier', 24, 'bold'))
    if len(hedefler) == 0:
        yaz.write('Tebrikler, kazandınız!', align='center', font=('Courier', 24, 'bold'))
