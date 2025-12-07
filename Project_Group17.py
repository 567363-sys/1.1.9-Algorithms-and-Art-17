import time
import turtle as trtl
import random as ran
import math
screen=trtl.Screen()
trtl.tracer(0)
p = trtl.Turtle()
p.speed(0)
screen.setup(800, 600)
screen.bgcolor("Wheat2")  # dark background to make the glow pop

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
# Static drawer (wreath and decorations)
drawer = trtl.Turtle()
drawer.hideturtle()
drawer.speed(0)
drawer.pensize(2)

def draw_wreath():
    drawer.clear()
    # base ring
    cx, cy = 0, -40
    outer_r = 80
    inner_r = 40

    # draw outer green circle (thick)
    drawer.penup()
    drawer.goto(0, cy - outer_r)
    drawer.pendown()
    drawer.fillcolor("#0b6b2a")
    drawer.begin_fill()
    drawer.circle(outer_r)
    drawer.end_fill()

    # cut inner hole
    drawer.fillcolor('wheat2')
    drawer.penup()
    drawer.goto(0, cy - inner_r)
    drawer.pendown()
    drawer.begin_fill()
    drawer.circle(inner_r)
    drawer.end_fill()

    # draw layered leaves around the ring
    drawer.penup()
    leaf_count = 60
    for i in range(leaf_count):
        ang = 360 * i / leaf_count
        rad = (outer_r + inner_r) / 2
        x = cx + rad * math.cos(math.radians(ang))
        y = cy + rad * math.sin(math.radians(ang))
        drawer.goto(x, y)
        drawer.setheading(ang + 90)
        # draw a leaf as a small filled ellipse-like shape using circle segments
        drawer.fillcolor(ran.choice(["#2f8a44", "#2b7e3f", "#1f6a33"]))
        drawer.begin_fill()
        drawer.pendown()
        drawer.forward(18)
        drawer.right(40)
        drawer.circle(10, 100)
        drawer.right(80)
        drawer.forward(18)
        drawer.end_fill()
        drawer.penup()

draw_wreath()

class SteamPuff(trtl.Turtle):
    def __init__(self, x_pos, y_pos):  
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("#000000")
        self.goto(x_pos, y_pos)
        self.size = ran.randint(5, 15)  
        self.setheading(90)  
        self.speed(0) #max speed

    def move(self):
        if self.size > 10:
            self.color("black")
        elif self.size > 5:
            self.color("black")
        else:
            self.color("black")
        
        self.shapesize(self.size / 20)  
        self.forward(ran.uniform(0.5, 1.5)) 
        self.size -= 0.1   #should not go smaller than that otherwise code will stop

steam_puffs = []  #new index for class steampuff 
def create_steam():  #Note: Technically animation code, want to keep loop cleaner
    x = ran.randint(-15, 15)  
    y = -200 # 
    new_puff = SteamPuff(x, y)
    steam_puffs.append(new_puff)

def animate():
    screen.update()  
    
    
    if ran.random() < 0.2:
        create_steam()
    
    
    for puff in steam_puffs:
        puff.move()
        if puff.size <= 0:
            puff.hideturtle()           
            steam_puffs.remove(puff)
#Candle
t = trtl.Turtle()

def goto(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

# Candle body
def draw_candle():
    t.color("light yellow")
    goto(-100, -100)
    t.begin_fill()
    for _ in range(2):
        t.forward(20)  # width
        t.left(90)
        t.forward(75)  # height
        t.left(90)
    t.end_fill()

# Wick
def draw_wick():
    t.color("black")
    t.pensize(3)
    goto(-90, -25)
    t.setheading(90)
    t.forward(10)

# --- Flame Animation ---

flame = trtl.Turtle()
flame.hideturtle()
flame.speed(0)

def draw_flame_frame():
    flame.clear()
    flame.penup()
    flame.goto(-85, -10)
    flame.setheading(90)
    flame.pendown()

    # Flicker by making the flame slightly wider/taller randomly
    wiggle = ran.randint(-2, 2)
    tall = ran.randint(15, 25)

    flame.color("orange")
    flame.begin_fill()
    flame.setheading(10)

    # Draw a simple teardrop flame shape
    for _ in range(18):
        flame.left(20)
        flame.forward(5 + wiggle)

    flame.left(25)
    for _ in range(18):
        flame.left(500)
        flame.forward(10 + wiggle / 3)

    flame.end_fill()


# --- Draw static objects ---
draw_candle()
draw_wick()



#Animation after this point (probably figure out some wierd loop to make it all run at once)
p.hideturtle()




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
  #smoke time
  animate()
  #smoke time is over
  
  # start animation for candle
  flametimer=4
  if flametimer%4 == 0:
    draw_flame_frame()
    flametimer=flametimer+1
  else:
    flametimer=flametimer+1
  time.sleep(0.05)
  trtl.update()   #update screen for animation
#Just realized we don't need the last part because of animation code!
