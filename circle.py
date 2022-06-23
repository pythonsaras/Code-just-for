from time import sleep
import turtle as tl

from pyparsing import line
tl.speed(20)
tl.bgcolor("black")
tl.pensize(2)
def cir(color):
    tl.pendown()
    tl.pencolor(color)
    tl.circle(50)
    
def squre(color):
    tl.pendown()
    tl.pencolor(color)
    tl.left(30)
    tl.forward(100)
    tl.left(40)
    tl.forward(50)
def arrow(color):
    tl.pendown()
    tl.pensize(1)
    tl.pencolor(color)
    tl.forward(100)
    tl.right(90)
    tl.forward(20)
    tl.left(135)
    tl.forward(35)
    tl.left(90)
    tl.forward(35)
    tl.left(135)
    tl.forward(20)
    tl.right(90)
    tl.forward(100)  
    tl.penup()

arrow("blue")
def heart(color):
    for i in range(90):
        tl.pendown()
        tl.pensize(1)
        tl.pencolor(color)
        tl.forward(10)
        if i<120:
            tl.right(i)
        else:
            tl.left(i)
        tl.penup() 

# heart("red")
for i in range(5):
    for color in ["red","green","blue","yellow","orange","white"]:
        pass
        # tl.pendown()
        # cir(color)
        # tl.left(30)
        # tl.forward(100)
        # tl.left(40)
        # tl.forward(10)
        # squre(color)
        # squre(color)
        # tl.penup()    
sleep(10)
