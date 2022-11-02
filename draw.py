# import turtle
# #get the instance of turtle
# t=turtle.Turtle()
# #select color
# t.color('#4285F4','#4285F4') ## RBG value of color
# #change the pen size
# t.pensize(5)
# #change the drawing speed
# t.speed(3)

# t.forward(120)
# t.right(90)
# t.circle(-150,50)  ## first circle for red color
# t.color('#0F9D58')
# t.circle(-150,100)
# t.color('#F4B400')
# t.circle(-150,60)
# t.color('#DB4437','#DB4437')

# t.begin_fill()
# t.circle(-150,100)
# t.right(90)
# t.forward(50)
# t.right(90)
# t.circle(100,100)
# t.right(90)
# t.forward(50)
# t.end_fill()

# t.begin_fill()

# ## second circle for yellow color

# t.color("#F4B400","#F4B400")
# t.right(180)
# t.forward(50)
# t.right(90)

# t.circle(100,60)
# t.right(90)
# t.forward(50)
# t.right(90)
# t.circle(-150,60)
# t.end_fill()


# # third circle of green color
# t.right(90)
# t.forward(50)
# t.right(90)
# t.circle(100,60)
# t.color('#0F9D58','#0F9D58')
# t.begin_fill()
# t.circle(100,100)
# t.right(90)
# t.forward(50)
# t.right(90)
# t.circle(-150,100)
# t.right(90)
# t.forward(50)
# t.end_fill()


# ##Draw last circle

# t.right(90)
# t.circle(100,100)
# t.color('#4285F4','#4285F4')
# t.begin_fill()
# t.circle(100,25)
# t.left(115)
# t.forward(65)
# t.right(90)
# t.forward(42)
# t.right(90)
# t.forward(124)
# t.right(90)
# t.circle(-150,50)
# t.right(90)
# t.forward(50)

# t.end_fill()
# t.penup()



# ##Draw I love you with python
# import turtle

# draw = turtle.Turtle()

# def curve():
#     draw.pen(pencolor="white", pensize=3, speed=5)
#     for i in range(200):
#         draw.rt(1)
#         draw.fd(1)

# def heart():
#     draw.pen(pencolor="white",fillcolor="red", pensize=3, speed=5)
#     draw.shape("turtle")
#     draw.shapesize(1,1,1)
#     draw.begin_fill()
#     draw.lt(50)
#     draw.fd(113)
#     curve()
#     draw.lt(120)
#     curve()
#     draw.fd(112)
#     draw.end_fill()

#     draw.hideturtle()


# window = turtle.Screen()
# window.bgcolor('black')

# draw.penup()
# draw.goto(-80,300)
# draw.pendown()
# draw.shapesize(1,2,1)

# draw.pen(pencolor="white",fillcolor="yellow", pensize=3, speed=8)

# draw.begin_fill()

# draw.fd(160)
# draw.rt(90)
# draw.fd(25)
# draw.rt(90)
# draw.fd(60)
# draw.lt(90)

# draw.fd(140)
# draw.lt(90)
# draw.fd(60)
# draw.rt(90)
# draw.fd(25)
# draw.rt(90)
# draw.fd(160)
# draw.rt(90)
# draw.fd(25)
# draw.rt(90)
# draw.fd(60)
# draw.lt(90)
# draw.fd(140)
# draw.left(90)
# draw.fd(60)
# draw.rt(90)
# draw.fd(25)

# draw.end_fill()

# draw.penup()
# draw.goto(-550,-20)
# draw.pendown()

# draw.pen(pencolor="white",fillcolor="yellow", pensize=3, speed=2)
# draw.begin_fill()

# draw.rt(90)
# draw.fd(25)
# draw.rt(90)
# draw.fd(165)
# draw.lt(90)
# draw.fd(115)
# draw.rt(90)
# draw.fd(25)
# draw.rt(90)
# draw.fd(140)
# draw.rt(90)
# draw.fd(190)
# draw.rt(90)

# draw.end_fill()

# draw.penup()
# draw.fd(140)

# draw.fd(70)

# draw.pen(pencolor="white",fillcolor="yellow", pensize=3, speed=8)
# draw.begin_fill()

# draw.rt(90)
# draw.fd(190)
# draw.lt(90)
# draw.pendown()
# draw.circle(60)
# draw.lt(90)
# draw.penup()
# draw.fd(20)
# draw.rt(90)
# draw.pendown()
# draw.circle(40)
# draw.rt(90)
# draw.penup()
# draw.fd(20)
# draw.lt(90)

# draw.end_fill()

# draw.fd(100)
# draw.pendown()

# draw.pen(pencolor="white",fillcolor="yellow", pensize=3, speed=8)
# draw.begin_fill()

# draw.lt(100)
# draw.fd(120)
# draw.rt(100)
# draw.fd(20)
# draw.rt(80)
# draw.fd(100)
# draw.lt(80)
# draw.fd(20)
# draw.lt(80)
# draw.fd(100)
# draw.rt(80)
# draw.fd(20)
# draw.rt(100)
# draw.fd(120)
# draw.rt(80)
# draw.fd(50)
# draw.lt(180)

# draw.end_fill()

# draw.penup()
# draw.fd(100)
# draw.pendown()

# draw.pen(pencolor="white",fillcolor="yellow", pensize=3, speed=8)
# draw.begin_fill()

# draw.lt(90)
# draw.fd(120)
# draw.rt(90)
# draw.fd(80)
# draw.rt(90)
# draw.fd(20)
# draw.rt(90)
# draw.fd(60)
# draw.lt(90)
# draw.fd(30)
# draw.lt(90)
# draw.fd(60)
# draw.rt(90)
# draw.fd(20)
# draw.rt(90)
# draw.fd(60)
# draw.lt(90)
# draw.fd(30)
# draw.lt(90)
# draw.fd(60)
# draw.rt(90)
# draw.fd(20)
# draw.rt(90)
# draw.fd(80)

# draw.end_fill()

# draw.penup()
# draw.rt(180)
# draw.fd(200)
# draw.pendown()


# draw.pen(pencolor="white",fillcolor="yellow", pensize=3, speed=2)
# draw.begin_fill()

# draw.lt(90)
# draw.fd(50)
# draw.lt(30)
# draw.fd(80)
# draw.rt(120)
# draw.fd(20)
# draw.rt(60)
# draw.fd(60)
# draw.lt(180)
# draw.rt(60)
# draw.fd(60)
# draw.rt(60)
# draw.fd(20)
# draw.rt(120)
# draw.fd(80)
# draw.lt(30)
# draw.fd(50)
# draw.rt(90)
# draw.fd(20)
# draw.rt(180)

# draw.end_fill()

# draw.penup()
# draw.fd(120)
# draw.pendown()


# draw.pen(pencolor="white",fillcolor="yellow", pensize=3, speed=8)
# draw.begin_fill()

# draw.circle(60)
# draw.lt(90)
# draw.penup()
# draw.fd(20)
# draw.pendown()
# draw.rt(90)
# draw.circle(40)
# draw.rt(90)
# draw.penup()
# draw.fd(20)
# draw.lt(90)

# draw.end_fill()

# draw.fd(100)
# draw.circle(60, extent=60)
# draw.pendown()

# draw.pen(pencolor="white",fillcolor="yellow", pensize=3, speed=8)
# draw.begin_fill()

# draw.lt(30)

# draw.fd(85)
# draw.lt(90)
# draw.fd(20)
# draw.lt(90)
# draw.fd(70)
# draw.circle(-20, extent=180)
# draw.fd(70)
# draw.lt(90)

# draw.fd(20)
# draw.lt(90)
# draw.fd(85)
# draw.circle(40, extent=180)

# draw.end_fill()

# draw.penup()

# draw.rt(180)
# draw.fd(35)
# draw.lt(90)
# draw.fd(140)
# draw.lt(90)
# draw.pendown()

# heart()

# turtle.done()


## Wraw Doraemona
from turtle import *


# Doraemon with Python Turtle
def ankle(x, y):
    penup()
    goto(x, y)
    pendown()


def eyes():
    fillcolor("#ffffff")
    begin_fill()

    tracer(False)
    a = 2.5
    for i in range(120):
        if 0 <= i < 30 or 60 <= i < 90:
            a -= 0.05
            lt(3)
            fd(a)
        else:
            a += 0.05
            lt(3)
            fd(a)
    tracer(True)
    end_fill()


def daari():
    ankle(-32, 135)
    seth(165)
    fd(60)

    ankle(-32, 125)
    seth(180)
    fd(60)

    ankle(-32, 115)
    seth(193)
    fd(60)

    ankle(37, 135)
    seth(15)
    fd(60)

    ankle(37, 125)
    seth(0)
    fd(60)

    ankle(37, 115)
    seth(-13)
    fd(60)


def mukh():
    ankle(5, 148)
    seth(270)
    fd(100)
    seth(0)
    circle(120, 50)
    seth(230)
    circle(-120, 100)


def scarf():
    fillcolor('#e70010')
    begin_fill()
    seth(0)
    fd(200)
    circle(-5, 90)
    fd(10)
    circle(-5, 90)
    fd(207)
    circle(-5, 90)
    fd(10)
    circle(-5, 90)
    end_fill()


def nose():
    ankle(-10, 158)
    seth(315)
    fillcolor('#e70010')
    begin_fill()
    circle(20)
    end_fill()


def black_eyes():
    seth(0)
    ankle(-20, 195)
    fillcolor('#000000')
    begin_fill()
    circle(13)
    end_fill()

    pensize(6)
    ankle(20, 205)
    seth(75)
    circle(-10, 150)
    pensize(3)

    ankle(-17, 200)
    seth(0)
    fillcolor('#ffffff')
    begin_fill()
    circle(5)
    end_fill()
    ankle(0, 0)


def face():
    fd(183)
    lt(45)
    fillcolor('#ffffff')
    begin_fill()
    circle(120, 100)
    seth(180)
    # print(pos())
    fd(121)
    pendown()
    seth(215)
    circle(120, 100)
    end_fill()
    ankle(63.56, 218.24)
    seth(90)
    eyes()
    seth(180)
    penup()
    fd(60)
    pendown()
    seth(90)
    eyes()
    penup()
    seth(180)
    fd(64)


def taauko():
    penup()
    circle(150, 40)
    pendown()
    fillcolor('#00a0de')
    begin_fill()
    circle(150, 280)
    end_fill()


def Doraemon():
    taauko()

    scarf()

    face()

    nose()

    mukh()

    daari()

    ankle(0, 0)

    seth(0)
    penup()
    circle(150, 50)
    pendown()
    seth(30)
    fd(40)
    seth(70)
    circle(-30, 270)

    fillcolor('#00a0de')
    begin_fill()

    seth(230)
    fd(80)
    seth(90)
    circle(1000, 1)
    seth(-89)
    circle(-1000, 10)

    # print(pos())

    seth(180)
    fd(70)
    seth(90)
    circle(30, 180)
    seth(180)
    fd(70)

    # print(pos())
    seth(100)
    circle(-1000, 9)

    seth(-86)
    circle(1000, 2)
    seth(230)
    fd(40)

    # print(pos())

    circle(-30, 230)
    seth(45)
    fd(81)
    seth(0)
    fd(203)
    circle(5, 90)
    fd(10)
    circle(5, 90)
    fd(7)
    seth(40)
    circle(150, 10)
    seth(30)
    fd(40)
    end_fill()

    seth(70)
    fillcolor('#ffffff')
    begin_fill()
    circle(-30)
    end_fill()

    ankle(103.74, -182.59)
    seth(0)
    fillcolor('#ffffff')
    begin_fill()
    fd(15)
    circle(-15, 180)
    fd(90)
    circle(-15, 180)
    fd(10)
    end_fill()

    ankle(-96.26, -182.59)
    seth(180)
    fillcolor('#ffffff')
    begin_fill()
    fd(15)
    circle(15, 180)
    fd(90)
    circle(15, 180)
    fd(10)
    end_fill()

    ankle(-133.97, -91.81)
    seth(50)
    fillcolor('#ffffff')
    begin_fill()
    circle(30)
    end_fill()
    # Doraemon with Python Turtle

    ankle(-103.42, 15.09)
    seth(0)
    fd(38)
    seth(230)
    begin_fill()
    circle(90, 260)
    end_fill()

    ankle(5, -40)
    seth(0)
    fd(70)
    seth(-90)
    circle(-70, 180)
    seth(0)
    fd(70)

    ankle(-103.42, 15.09)
    fd(90)
    seth(70)
    fillcolor('#ffd200')
    # print(pos())
    begin_fill()
    circle(-20)
    end_fill()
    seth(170)
    fillcolor('#ffd200')
    begin_fill()
    circle(-2, 180)
    seth(10)
    circle(-100, 22)
    circle(-2, 180)
    seth(180 - 10)
    circle(100, 22)
    end_fill()
    goto(-13.42, 15.09)
    seth(250)
    circle(20, 110)
    seth(90)
    fd(15)
    dot(10)
    ankle(0, -150)

    black_eyes()


if __name__ == '__main__':
    screensize(800, 600, "#f0f0f0")
    pensize(3)
    speed(9)
    Doraemon()
    ankle(100, -300)
    mainloop()