import turtle as tl
import random

width=500
height=500
food_size=10
delay=100

offsets={
    'up':(0,20),
    'down':(0,-20),
    'left':(-20,0),
    'right':(20,0)
}

def reset():
    global snake,snake_dir,food_pos,pen
    snake=[[0,0],[0,20],[0,40],[0,50],[0,60]]
    snake_dir='up'
    food_pos=get_random_food_pos()
    food.goto(food_pos)
    move_snake()

def move_snake():
    global snake_dir
    new_head=snake[-1].copy()
    new_head[0]=snake[-1][0]+offsets[snake_dir][0]
    new_head[1]=snake[-1][1]+offsets[snake_dir][1]

    if new_head in snake[:-1]:
        reset()
    else:
        snake.append(new_head)
        if not food_collision():
            snake.pop(0)
        if snake[-1][0]>width/2:
            snake[-1][0]-=width
        elif snake[-1][0]<-width/2:
            snake[-1][0]+=width
        elif snake[-1][1]>height/2:
            snake[-1][1] -=height
        elif snake[-1][1]<-height/2:
            snake[-1][1]+=height

        pen.clearstamps()

        for segment in snake:
            pen.goto(segment[0],segment[1])
            pen.stamp()

        screen.update()
        tl.ontimer(move_snake,delay)

def food_collision():
    global food_pos
    if get_distance(snake[-1],food_pos)<20:
        food_pos=get_random_food_pos()
        food.goto(food_pos)
        return True
    return False
def get_random_food_pos():
    x=random.randint(-width/2+food_size,width/2-food_size)
    y=random.randint(-height/2+food_size,height/2-food_size)
    return (x,y)    
def get_distance(pos1,pos2):
    x1,y1=pos1
    x2,y2=pos2
    distance=((y2-y1)**2+(x2-x1)**2)**0.5
    return distance
def go_up():
    global snake_dir
    if snake_dir!='down':
        snake_dir='up'
def go_right():
    global snake_dir
    if snake_dir!='left':
        snake_dir='right'
def go_down():
    global snake_dir
    if snake_dir!='up':
        snake_dir='down'
def go_left():
    global snake_dir
    if snake_dir!='right':
        snake_dir='left'
        
screen=tl.Screen()
screen.setup(width,height)
screen.title("Snake")
screen.bgcolor("green")
screen.setup(500,500)
screen.tracer(0)
pen=tl.Turtle("square")
pen.penup()

food=tl.Turtle()
food.shape("circle")
food.color('red')
food.shapesize(food_size/20)
food.penup()

screen.listen()
screen.onkey(go_up,'Up')
screen.onkey(go_right,'Right')
screen.onkey(go_down,'Down')
screen.onkey(go_left,'Left')

reset()
tl.done()


