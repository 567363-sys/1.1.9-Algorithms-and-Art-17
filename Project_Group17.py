#   a113_long_circle.py
#   Draw a circle calling only the forward and
#   right methods
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



#Extra still drwaing code goes here!!!!!


#Animation after this point (probably figure out some wierd loop to make it all run at once)


wn = trtl.Screen()
wn.mainloop()
