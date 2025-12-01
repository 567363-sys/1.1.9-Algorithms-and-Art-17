import time
import turtle as trtl
import random as ran
p = trtl.Turtle()
p.speed(0)

#Background
p.penup()
p.goto(1000, 1000)
p.fillcolor('wheat2')
p.begin_fill()
p.goto(-1000, 1000)
p.goto(-1000, -1000)
p.goto(1000, -1000)
p.goto(1000,1000)
p.goto(-1000, 1000)
p.end_fill()
p.penup()

# Outlines
p.pensize(5)
p.penup()
p.pensize(2)
p.goto(-140,40)
p.pendown()
p.fillcolor('grey20')
p.begin_fill()
for i in range(2):
  p.forward(100)
  p.left(90)
  p.forward(130)
  p.left(90)
p.penup()
p.pensize(2)
p.goto(50,40)
p.pendown()
for i in range(2):
  p.forward(100)
  p.left(90)
  p.forward(130)
  p.left(90)
p.end_fill()
#Inner lines
p.pensize(5)
p.penup()
p.goto(-90,40)
p.left(90)
p.pendown()
p.forward(130)
p.penup()
p.goto(-40,105)
p.pendown()
p.left(90)
p.forward(100)

p.penup()
p.goto(100,40)
p.right(90)
p.pendown()
p.forward(130)
p.penup()
p.goto(150,105)
p.pendown()
p.left(90)
p.forward(100)
p.penup()



#Extra still drawing code goes here!!!!!


#Animation after this point (probably figure out some wierd loop to make it all run at once)
p.hideturtle()
screen=trtl.Screen()
trtl.tracer(0)




snowflakes = []
secondwindow = []
for i in range(5):  #Makes first snowflakes
  actsnow = trtl.Turtle()
  actsnow.hideturtle()
  actsnow.setheading(270)
  actsnow.penup()
  actsnow.goto(ran.randint(-130, -50), 169)
  actsnow.shape('circle')
  actsnow.color('white')
  actsnow.shapesize(stretch_wid= .1, stretch_len= .1)
  snowflakes.append(actsnow)
for i in range(5):  #Makes second window snowflakes
  actsnow = trtl.Turtle()
  actsnow.hideturtle()
  actsnow.setheading(270)
  actsnow.penup()
  actsnow.goto(ran.randint(60, 140), 169)
  actsnow.shape('circle')
  actsnow.color('white')
  actsnow.shapesize(stretch_wid= .1, stretch_len= .1)
  secondwindow.append(actsnow)
alternate = 1
x=1
while x == 1: #infinite loop

#SNOWFLAKES!
  if alternate%30 == 0:
    actsnow = trtl.Turtle()
    actsnow.hideturtle()
    actsnow.setheading(270)
    actsnow.penup()
    actsnow.goto(ran.randint(-130, -50), 169)
    actsnow.shape('circle')
    actsnow.color('white')
    actsnow.shapesize(stretch_wid= .1, stretch_len= .1)
    if -95< actsnow.xcor()<-85 :   #no more snow on middle line(almost)   (FIXED IT)
      actsnow.hideturtle()
    else:
      snowflakes.append(actsnow)
  
  s1=ran.choice(snowflakes)
  s2=ran.choice(snowflakes)
  s3=ran.choice(snowflakes)
  s4=ran.choice(snowflakes)
  s1.showturtle()
  s2.showturtle()
  s3.showturtle()
  s4.showturtle()   #moves snow
  s1.forward(ran.randint(3,10))
  s2.forward(ran.randint(8,15))
  s3.forward(ran.randint(3,10))
  s4.forward(ran.randint(8,15))


  if 100 < s1.ycor() <110:   #Hide turtle behind window bar
    s1.hideturtle()
  else:
    s1.showturtle()
  if 100 < s2.ycor() <110:
    s2.hideturtle()
  else:
    s2.showturtle()
  if 100 <s3.ycor()<110:
    s3.hideturtle()
  else:
    s3.showturtle()
  if 100 < s4.ycor() <110:
    s4.hideturtle()
  else:
    s4.showturtle()


  if s1.ycor() > 40:   #gets rid of snow below window
    snowflakes.append(s1)
  else:
    s1.hideturtle()
  if s2.ycor() > 40:
    snowflakes.append(s2)
  else:
    s2.hideturtle()
  if s3.ycor() > 40:
    snowflakes.append(s3)
  else:
    s3.hideturtle()
  if s4.ycor() > 40:
    snowflakes.append(s4)
  else:
    s4.hideturtle()
    
  
    #Second window
  if alternate%30 == 0:
    actsnow = trtl.Turtle()
    actsnow.hideturtle()
    actsnow.setheading(270)
    actsnow.penup()
    actsnow.goto(ran.randint(60, 140), 169)
    actsnow.shape('circle')
    actsnow.color('white')
    actsnow.shapesize(stretch_wid= .1, stretch_len= .1)
    secondwindow.append(actsnow)
    alternate=alternate+1
    if 105> actsnow.xcor()>95:
      actsnow.hideturtle
    else:
      snowflakes.append(actsnow)
  else:
    alternate=alternate+1
  s1=ran.choice(secondwindow)
  s2=ran.choice(secondwindow)
  s3=ran.choice(secondwindow)
  s4=ran.choice(secondwindow)
  s1.showturtle()
  s2.showturtle()
  s3.showturtle()
  s4.showturtle()   #moves snow
  s1.forward(ran.randint(3,10))
  s2.forward(ran.randint(8,15))
  s3.forward(ran.randint(3,10))
  s4.forward(ran.randint(8,15))
  
  


  if 100 < s1.ycor() <110:   #Hide turtle behind window bar
    s1.hideturtle()
  else:
    s1.showturtle()
  if 100 < s2.ycor() <110:
    s2.hideturtle()
  else:
    s2.showturtle()
  if 100 <s3.ycor()<110:
    s3.hideturtle()
  else:
    s3.showturtle()
  if 100 < s4.ycor() <110:
    s4.hideturtle()
  else:
    s4.showturtle()


  if s1.ycor() > 40:   #gets rid of snow below window
    secondwindow.append(s1)
  else:
    s1.hideturtle()
  if s2.ycor() > 40:
    secondwindow.append(s2)
  else:
    s2.hideturtle()
  if s3.ycor() > 40:
    secondwindow.append(s3)
  else:
    s3.hideturtle()
  if s4.ycor() > 40:
    secondwindow.append(s4)
  else:
    s4.hideturtle()
  time.sleep(.005)
  trtl.update()   #update screen for animation
#Just realized we don't need the last part because of animation code!
