#Turtle Graphics Game
import turtle
import math
import random
import playsound

wn=turtle.Screen()
wn.bgcolor("black")
wn.tracer(1.5)

#Draw border

mypen=turtle.Turtle()
mypen.color("white")
mypen.penup()
mypen.setposition(-200,-200)
mypen.pendown()
mypen.pensize(3)

for side in range(4):
    mypen.forward(400)
    mypen.left(90)

mypen.hideturtle()

#Create Player
player=turtle.Turtle()
player.color("blue")
player.shape("triangle")
player.up()

score=0

speed=2

#create villan
maxGoals=5
goals=[]

for count in range(maxGoals):
    goals.append(turtle.Turtle())
    goals[count].color("red")
    goals[count].shape("circle")
    goals[count].penup()
    goals[count].speed(0)
    goals[count].setposition(random.randint(-200,200),random.randint(-200,200))

#control player
def turnleft():
    player.left(30)

def turnright():
    player.right(30)

def increasespeed():
    global speed
    speed +=1

def isCollision(t1,t2):
    d=math.sqrt(math.pow(t1.xcor()-goals[count].xcor(),2)+math.pow(t1.ycor()-goals[count].ycor(),2))
    if d<20:
        return True
    else:
        return False
turtle.listen()
turtle.onkey(turnleft,"Left")
turtle.onkey(turnright,"Right")
turtle.onkey(increasespeed,"Up")


while True:
    player.forward(speed)
    #boundary checking
    if player.xcor()>190 or player.xcor()<-190:
            mypen.penup()
            mypen.hideturtle()
            mypen.setposition(0,0)
            scorstring1="Game Over.\nYour Score: %s"%score
            mypen.write(scorstring1,False,align="Left",font=("Arial",14,"normal"))
            break
    if player.ycor()>190 or player.ycor()<-190:
            mypen.penup()
            mypen.hideturtle()
            mypen.setposition(0,0)
            scorstring2="Game Over.\nYour Score: %s"%score
            mypen.write(scorstring2,False,align="Left",font=("Arial",14,"normal"))
            break

    
    for count in range(maxGoals):
        goals[count].forward(3)

        #boundary checking
        if goals[count].xcor()>190 or goals[count].xcor()<-190:
            goals[count].right(180)
        if goals[count].ycor()>190 or goals[count].ycor()<-190:
            goals[count].right(180)
        
        #collision detection
        if isCollision(player,goals[count]):
            goals[count].setposition(random.randint(-180,180),random.randint(-180,180))
            goals[count].right(random.randint(0,360))
            score+=1
            
            #Draw the score in the screen
            mypen.undo()
            mypen.penup()
            mypen.hideturtle()
            mypen.setposition(-190,210)
            scorstring="Score: %s"%score
            mypen.write(scorstring,False,align="Left",font=("Arial",14,"normal"))

            #increase speed after each collision
            
            speed+=0.5
