from turtle import Turtle, Screen, mainloop

oyna = Screen()
oyna.title('Uchar Toshbaqa')

chiziq =Turtle()
chiziq.color('red')
chiziq.pensize(15)
chiziq.speed(0)
chiziq.hideturtle()
chiziq.up()
chiziq.goto(300, 300)
chiziq.down()
chiziq.goto(300, -300)
chiziq.goto(-300, -300)
chiziq.goto(-300, 300)
chiziq.goto(300, 300)

koptok = Turtle()
koptok.shape('arrow')
koptok.color('black', 'green')
koptok.shapesize(5)
koptok.up()
koptok.goto(0, 0)



step_x = 3
step_y = 2
while True:
    x, y = koptok.position()

    if x + step_x >= 300 or x + step_x <+ -300:
        step_x = -step_x
    if y + step_y >= 300 or y + step_y <= -300:
        step_y = -step_y
    
    koptok.goto(x+step_x, y+step_y)



mainloop()
