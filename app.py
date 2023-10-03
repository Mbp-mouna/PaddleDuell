# turtle: module pour les grapique vectoriel
import turtle 




wind = turtle.Screen()#création de window de l'app
wind.title("Ping pong by Mouna")
wind.bgcolor("black")
wind.setup(width=800, height=600)
wind.tracer(0)#stop the window from updating automatically


#padle1

padle1 = turtle.Turtle()
padle1.speed()
padle1.shape("square")
padle1.shapesize(stretch_wid=5, stretch_len=1)
padle1.color("blue")
padle1.penup()
padle1.goto(-350,0)

#padle2
padle2 = turtle.Turtle()
padle2.speed()
padle2.shape("square")
padle2.shapesize(stretch_wid=5, stretch_len=1)#stretches the shape to meet the size
padle2.color("red")
padle2.penup()
padle2.goto(350,0)

#ball

ball = turtle.Turtle()#initializes turtle object(shape)
ball.speed() #set the speed of the animation
ball.shape("circle") #set the shape of the object
ball.color("green") #set the color of the shape
ball.penup() #stop the object from drawing lines 
ball.goto(0,0)#et the position of object
ball.dx=0.25
ball.dy=0.25

#score
score1= 0
score2= 0
score= turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(0,260)
score.write("Player 1 : 0   Player 2: 0",align="center",font=("courier",24,"normal"))
#funtions
def padle1_up():
    y=padle1.ycor()#get the y coordinate of the padle 1
    y+=20# set the u to increase be 20
    padle1.sety(y)#set the y of the padle1 to the new y coordinate

def padle1_down():
    y=padle1.ycor()
    y-=20
    padle1.sety(y)

def padle2_up():
    y=padle2.ycor()
    y+=20
    padle2.sety(y)

def padle2_down():
    y=padle2.ycor()
    y-=20
    padle2.sety(y)
#keyboard bindings
wind.listen() #tell the window to except keyboard input
wind.onkeypress(padle1_up,"a") #when pressing a the function padle1_up is invoked
wind.onkeypress(padle1_down,"q")
wind.onkeypress(padle2_up,"Up")
wind.onkeypress(padle2_down,"Down")
 
#main game loop
while True :
  wind.update()#  update the screen everytime the loop run
 #mov the ball
  ball.setx(ball.xcor()+ball.dx) #ball statrts at 0 and everytime loops run------>+0.5 xaxis
  ball.sety(ball.ycor()+ball.dy) #ball statrts at 0 and everytime loops run------>+0.5 yaxis
 
 #border check,top border+300px,bottom border -300px,ball is 20 px
  if ball.ycor() >290:#if ball is at top border
    ball.sety(290) # set y coordinate +290
    ball.dy*=-1 # reverse direction, making +0.5------>-0.5

  if ball.ycor() <-290:
     ball.sety(-290)
     ball.dy*=-1

  if ball.xcor()>390:
     ball.goto(0,0)
     ball.dx*=-1
     score1+=1
     score.clear()
     score.write("Player 1 : {}   Player 2: {}".format(score1,score2),align="center",font=("courier",24,"normal"))

  if ball.xcor()<-390:
     ball.goto(0,0)
     ball.dx*=-1
     score2+=1
     score.clear()
     score.write("Player 1 : {}   Player 2: {}".format(score1,score2),align="center",font=("courier",24,"normal"))

#collision padle and ball
  if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < padle2.ycor() + 40 and  ball.ycor() > padle2.ycor() - 40):
    ball.setx(330)
    ball.dx*=-1

  if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < padle1.ycor() + 40 and  ball.ycor() > padle1.ycor() - 40):
    ball.setx(-340)
    ball.dx*=-1



  