import turtle

def funk1():
    tosh.forward(100)

def funk2():
    tosh.left(45)

def funk3():
    tosh.right(45)

def funk4():
    tosh.forward(-100)

def main():
    global tosh
    global wn


    wn = turtle.Screen()
    wn.setup(700, 700)
    wn.title("Toshbaqa")
    wn.bgcolor("black")
    

    tosh = turtle.Turtle()
    tosh.shape("turtle")
    tosh.shapesize(3)
    tosh.color("black", "green")

    wn.onkey(funk1, "Up")
    wn.onkey(funk2, "Left")
    wn.onkey(funk3, "Right")
    wn.onkey(funk4, "Down")
    

    wn.listen()
    wn.mainloop()
main()