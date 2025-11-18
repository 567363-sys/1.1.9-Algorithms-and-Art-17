#   a113_long_circle.py
#   Draw a circle calling only the forward and
#   right methods
import turtle as trtl

p = trtl.Turtle()

# Outlines
p.penup()
p.pensize(2)
p.goto(-140,40)
p.pendown()
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
#extra still drawing goes here

#animation after this point

wn = trtl.Screen()
wn.mainloop()
