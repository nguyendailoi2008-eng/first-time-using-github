#HELLO WORLD, this is my first project (kinda?)!!! instructions from TokyoEdtech (youtube)
#imports
import turtle
import time
import random

delay=0.1
segments=[]

a=int(input("ENTER PASSWORD: "))
if a==1:
   print("welcome!")
else:
   print("wrong!!!, but enjoy the game tho")



    # setups
wdw = turtle.Screen()
wdw.title('my first game')
wdw.bgcolor('green')
wdw.setup(width=600, height=600)
wdw.tracer(0)  # turns OFF screen update

    # border
drawer = turtle.Turtle()
drawer.hideturtle()
drawer.pensize(3)
drawer.color('red')
drawer.penup()
drawer.goto(291, 0)
drawer.pendown()
drawer.left(90)
drawer.forward(291)
drawer.left(90)
drawer.forward(582)
drawer.left(90)
drawer.forward(582)
drawer.left(90)
drawer.forward(582)
drawer.left(90)
drawer.forward(291)
drawer.penup()

    # snakehead
head = turtle.Turtle()
head.speed(0)
head.shape('circle')
head.color('black')
head.penup()
head.goto(0, 0)
head.direction = "stop"

    # snake food
food = turtle.Turtle()
food.speed(0)
food.shape('circle')
food.color('red')
food.penup()
food.goto(0, 100)

    # scoring
current = 0
highest = 0
pen = turtle.Turtle()
pen.speed(0)
pen.shape('square')
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0, 300)
pen.write('<current:0>   <highest:0>', align='center', font=('Courier', 20, 'normal'))

    # FUNCTIONS

    # directions 1
def up():
    if head.direction != "down":
        head.direction = "up"

def down():
    if head.direction != "up":
            head.direction = "down"

def left():
    if head.direction != "right":
            head.direction = "left"

def right():
    if head.direction != "left":
            head.direction = "right"

t=10
    # directions 2
def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + t)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - t)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + t)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - t)

    # keybinds
wdw.listen()
wdw.onkey(up, "Up")
wdw.onkey(down, "Down")
wdw.onkey(left, "Left")
wdw.onkey(right, "Right")


#main game loop
while True:
    wdw.update()
#check for border collisions:
    if head.xcor()==290 or head.xcor()==-290 or head.ycor()==290 or head.ycor()==-290:
        time.sleep(1)
        head.goto(0,0)
        head.direction="stop"

        # reset score
        current = 0
        pen.clear()
        pen.write("<current:{}>   <highest:{}>".format(current, highest), align='center',
                  font=('Courier', 20, 'normal'))
         #hide segments
        for segment in segments:
            segment.goto(10000,10000)
        #clear segments list
        segments.clear()
    #body, head, food, pooisonous berries relations
    if head.distance(food)<20:

        # make food move after collison:
        x=random.randint(-280,280)
        y=random.randint(-280,280)
        food.goto(x,y)

        # body
        body=turtle.Turtle()
        body.speed(0)
        body.shape('circle')
        body.color('grey')
        body.penup()
        #grow after eating
        segments.append(body)

        #score count
        current +=10
        if current>highest:
            highest=current

        pen.clear()
        pen.write("<current:{}>   <highest:{}>".format(current, highest), align='center', font=('Courier', 20, 'normal'))
    #stick the body to the head (move tail segments towards neck)
    for index in range(len(segments)-1,0,-1):
        x=segments[index-1].xcor()
        y=segments[index-1].ycor()
        segments[index].goto(x,y)
    #move segment 0 to head
    if len(segments)>0:
        x=head.xcor()
        y=head.ycor()
        segments[0].goto(x,y)
    move()

    #die when touching yourself....????
    for segment in segments:
        if segment.xcor()==head.xcor() and segment.ycor()==head.ycor():
            head.direction="stop"
            head.goto(0,0)



            for segment in segments:
                segment.goto(10000, 10000)
            # clear segments list
            segments.clear()
            #reset score
            current =0
            pen.clear()
            pen.write("<current:{}>   <highest:{}>".format(current, highest), align='center',
                      font=('Courier', 20, 'normal'))

     #ENDGAME
    if current==highest==100000:
        head.direction="stop"
        for segment in segments:
            segment.goto(10000, 10000)
        # clear segments list
        segments.clear()
        pen.clear()
        pen.write("you've won!!!!", align='center', font=('Courier', 50, 'normal'))
        turtle.done()

    time.sleep(delay)








