import turtle
import time
import random


delay = 0.1

#score

score = 0
high_score = 0

#set up the screen

wn = turtle.Screen()

wn.title("Snake Game")
wn.bgcolor("green")
wn.setup(width=1050,height=1050)
wn.tracer(0) #turns off the screen updates

#snake head

head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color('black')
head.penup()
head.goto(0,0)

head.direction = "stop"


#Snake food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color('red')
food.penup()
food.goto(0,100)

segments = []
#Pen

pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0,490)
pen.write("Score: {}  High Score: {}".format(score,high_score),align = 'center', font=("Courier",24,"normal"))

#functions

def go_up():
    if head.direction != 'down':
        head.direction = 'up'
def go_down():
    if head.direction != 'up':
        head.direction = 'down'
def go_left():
    if head.direction != 'right':
        head.direction = 'left'
def go_right():
    if head.direction != 'left':
        head.direction = 'right'



def move():
    if head.direction == 'up':
        y = head.ycor()
        head.sety(y+20)
    if head.direction == 'down':
        y = head.ycor()
        head.sety(y-20)
    if head.direction == 'left':
        x = head.xcor()
        head.setx(x-20)
    if head.direction == 'right':
        x = head.xcor()
        head.setx(x+20)


#keyboard bindins
#connects a key press to a function call

wn.listen()

wn.onkeypress(go_up,'w')
wn.onkeypress(go_down,'s')
wn.onkeypress(go_left,'a')
wn.onkeypress(go_right,'d')


#Main game loop

while True:
    wn.update()

    #check for collision with border
    if head.xcor() > 500 or head.xcor() < -500 or head.ycor() > 500 or head.ycor()<-500:
        time.sleep(1)
        head.goto(0,0)
        head.direction = 'stop'
        
        #hide the segments
        for segment in segments:
            segment.goto(2000,2000)
        
        segments.clear()
        #shorten the delay
        delay = 0.1

        #Reset the score
        score = 0

        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score,high_score),align = 'center', font=("Courier",24,"normal"))

    #checking for collision with food
    if head.distance(food) < 20:
        # 20px if distance is less than 20px, means collision has occurred
        
        x = random.randint(-400,400)
        y = random.randint(-400,400)
        food.goto(x,y)

        # Add a segment to the object
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape('square')
        new_segment.color('grey')
        new_segment.penup()

        segments.append(new_segment)
        #shorten the delay
        delay -= 0.005
        #increase the score
        score += 10

        if score > high_score:
            high_score = score
        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score,high_score),align = 'center', font=("Courier",24,"normal"))

    # move the end segment first in reverse order

    for index in range(len(segments)-1,0,-1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()

        segments[index].goto(x,y)

    if len(segments)>0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)

    move()

    #check for collision with body and head

    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = 'stop'

            
            for segment in segments:
                segment.goto(2000,2000)
        
            segments.clear()
            #shorten the delay
            delay = 0.1

            #Reset the score
            score = 0

            pen.clear()
            pen.write("Score: {}  High Score: {}".format(score,high_score),align = 'center', font=("Courier",24,"normal"))

    time.sleep(delay)


wn.mainloop()


