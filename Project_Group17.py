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
#table
table=trtl.Turtle()
table.speed(0)
table.pencolor('brown')
table.fillcolor('sienna4')
table.penup()
table.begin_fill()
table.goto(-1000,-50)
table.pendown()
table.goto(1000,-50)
table.goto(1000,-1000)
table.goto(-1000,-1000)
table.goto(-1000,-50)
table.end_fill()


# Outlines
p.pensize(5)
p.penup()
p.pensize(2)
p.goto(-250,100)
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
p.goto(150,100)
p.pendown()
for i in range(2):
  p.forward(100)
  p.left(90)
  p.forward(130)
  p.left(90)
p.end_fill()

#Moon

turtle = trtl
trtl.penup()
trtl.hideturtle()
trtl.goto(-185,170)
trtl.begin_fill()
trtl.color("lightgrey")
trtl.circle(25)
trtl.end_fill()
trtl.color("black")
trtl.penup()
trtl.left(45)
trtl.forward(7)
trtl.pendown()
trtl.circle(5)
trtl.penup()
trtl.left(30)
trtl.forward(20)
trtl.pendown()
trtl.circle(4)
trtl.penup()
trtl.left(40)
trtl.forward(20)
trtl.pendown()
trtl.circle(7)
#Inner lines
p.pensize(5)
p.penup()
p.goto(-200,100)
p.left(90)
p.pendown()
p.forward(130)
p.penup()
p.goto(-150,165)
p.pendown()
p.left(90)
p.forward(100)

p.penup()
p.goto(200,100)
p.right(90)
p.pendown()
p.forward(130)
p.penup()
p.goto(250,165)
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
    cx, cy = 0, 200
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
    y = 100 # 
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
    goto(-300, -100)
    t.begin_fill()
    for _ in range(2):
        t.forward(25)  # width
        t.left(90)
        t.forward(80)  # height
        t.left(90)
    t.end_fill()

# Wick
def draw_wick():
    t.color("black")
    t.pensize(3)
    goto(-285, -20)
    t.setheading(90)
    t.forward(10)

# --- Flame Animation ---

flame = trtl.Turtle()
flame.hideturtle()
flame.speed(0)

def draw_flame_frame():
    flame.clear()
    flame.penup()
    flame.goto(-280, -5)
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
#Turkey!
t=trtl.Turtle()
t.up()
trtl.colormode(255)
def oval(x, y, w, h, color, angle=0, steps=100):
    t.color(color)
    pts = []
    for i in range(steps):
        a = 2*math.pi*i/steps
        px = (w/2)*math.cos(a)
        py = (h/2)*math.sin(a)

        rx = px*math.cos(math.radians(angle)) - py*math.sin(math.radians(angle))
        ry = px*math.sin(math.radians(angle)) + py*math.cos(math.radians(angle))
        pts.append((x+rx, y+ry))
    t.up()
    t.goto(pts[0])
    t.down()
    t.begin_fill()
    for p in pts:
        t.goto(p)
    t.end_fill()
    t.up()
def plate():
    oval(0,-60, 500,220, (180,180,180))
    oval(0,-50, 460,200, (225,225,225))
    oval(0,-48, 430,180, (245,245,245))

def turkey_body():
    oval(-10, 20, 260,150, (155,85,20), angle=-10)
    oval(-35, 40, 150,80, (210,130,50), angle=-15)
    oval(40, 10, 110,55, (120,60,15), angle=-10)
    oval(75, 5, 90,40, (90,45,10), angle=-8)
    oval(-90, 28, 85,42, (95,50,10), angle=-12)
def drumstick(x,y,flip=False):
    angle = -30 if not flip else 30
    oval(x, y, 100,130, (150,75,20), angle)
    oval(x+( -10 if not flip else 10), y+18, 70,90, (180,100,30), angle)
    oval(x+(18 if not flip else -18), y-12, 45,26, (100,50,15), angle)
    t.goto(x+(45 if not flip else -45), y-40)
    t.down()
    t.color((245,245,230))
    t.begin_fill()
    t.circle(14)
    t.end_fill()
    t.up()
def garnish():
    for dx,dy,w,h in [
        (-120,-55,60,25),
        (-50,-85,50,22),
        (25,-80,55,25),
        (110,-55,60,25)
    ]:
        oval(dx,dy, w,h, (40,130,60), angle=-30)
    for x,y in [(-150,-35),(150,-35)]:
        oval(x,y, 55,32, (255,240,70), angle=10)
        oval(x+5,y+5, 28,15, (255,255,160), angle=10)
    for x,y in [(-180,-20),(180,-20)]:
        oval(x,y, 40,30, (200,30,30))
        oval(x+3,y+4, 20,14, (255,120,120))
def texture():
    t.color((90,45,15))
    for x,y in [
        (-30,25),(5,35),(55,15),(-70,30),(95,10),
        (20,10),(-15,0),(45,-5),(-90,8)
    ]:
        t.goto(x,y)
        t.down()
        t.dot(7)
        t.up()
def steam():
    t.color((255,255,255))
    t.width(2)
    for x in [-40,0,40]:
        t.goto(x,110)
        t.down()
        t.setheading(90)
        for _ in range(25):
            t.forward(2)
            t.right(2)
        t.up()
    t.width(1)
def main():
    plate()
    turkey_body()
    drumstick(-170,-40,False)
    drumstick(150,-40,True)
    garnish()
    texture()
    steam()
    t.goto(0,-200)
    t.color((70,70,70))
main()


#Flowers
trtl.colormode(255)  # Enable RGB colors
t = trtl.Turtle()
t.speed(0)
t.hideturtle()
x_offset = 330  # Shift vase left
y_offset = 10
def draw_gradient_petal(x, y, radius, angle, start_color, end_color):
    t.penup()
    t.goto(x, y)
    t.pendown()
    layers = 5
    for i in range(layers):
        r = int(start_color[0] + (end_color[0]-start_color[0])*i/layers)
        g = int(start_color[1] + (end_color[1]-start_color[1])*i/layers)
        b = int(start_color[2] + (end_color[2]-start_color[2])*i/layers)
        t.fillcolor(r, g, b)
        t.begin_fill()
        t.circle(radius - i*3, angle)
        t.left(180 - angle)
        t.circle(radius - i*3, angle)
        t.left(180 - angle)
        t.end_fill()
def draw_flower(x, y, petals, radius):
    for i in range(petals):
        draw_gradient_petal(x, y, radius, 60, (255,50,50), (255,200,200))
        t.right(360/petals)
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor("yellow")
    t.begin_fill()
    t.circle(radius/5)
    t.end_fill()
def draw_leaf(x, y, scale):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color("green")
    t.begin_fill()
    t.setheading(ran.randint(20, 60))
    for _ in range(2):
        t.circle(15*scale,90)
        t.circle(7*scale,90)
    t.end_fill()
def draw_fancy_small_vase():
    base_x = x_offset
    base_y = y_offset - 150
    t.penup()
    t.goto(base_x, base_y)
    t.pendown()
    t.color("cyan4")
    t.begin_fill()
    # Curved sides
    t.goto(base_x-20, base_y)
    t.goto(base_x-35, base_y+70)
    t.goto(base_x-25, base_y+150)  # Neck
    t.goto(base_x+25, base_y+150)
    t.goto(base_x+35, base_y+70)
    t.goto(base_x+20, base_y)
    t.goto(base_x, base_y)
    t.end_fill()
    for i in range(6):
        t.penup()
        t.goto(base_x-25 + i*5, base_y+5*i)
        t.pendown()
        t.color((160+i*8,82+i*5,45+i*3))
        t.goto(base_x-25 + i*5, base_y+70 - 5*i)
    t.penup()
    t.color("gold")
    for y in range(base_y+10, base_y+70, 15):
        t.goto(base_x-10, y)
        t.pendown()
        t.dot(5)
        t.penup()
        t.goto(base_x+10, y+5)
        t.pendown()
        t.dot(5)
    t.penup()
    t.goto(base_x-25, base_y+150)
    t.pendown()
    t.width(2)
    t.goto(base_x+25, base_y+150)
    t.width(1)
draw_fancy_small_vase()
flower_positions = [(0, 0), (-20, 15), (20, 20), (-10, 30), (10, 35)]
flower_radii = []
for pos in flower_positions:
    radius = ran.randint(30,45)
    flower_radii.append(radius)
    draw_flower(pos[0]+x_offset, pos[1]+y_offset, petals=ran.randint(6,9), radius=radius)
leaf_positions = [(-35, -10), (35, -20), (-15, 5), (15, 10), (0, 25)]
t.color("green")
t.width(3)
for pos, radius in zip(flower_positions, flower_radii):
    t.penup()
    t.goto(pos[0]+x_offset, pos[1]-radius/2+y_offset)
    t.pendown()
    t.goto(pos[0]+x_offset, y_offset-80)
t.width(1)
t.hideturtle()

#Animation after this point (probably figure out some wierd loop to make it all run at once)
p.hideturtle()




snowflakes = []
secondwindow = []
for i in range(5):  #Makes first snowflakes
  actsnow = trtl.Turtle()
  actsnow.hideturtle()
  actsnow.setheading(270)
  actsnow.penup()
  actsnow.goto(ran.randint(-245, -150), 230)
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
    actsnow.goto(ran.randint(-240, -150), 230)
    actsnow.shape('circle')
    actsnow.color('white')
    actsnow.shapesize(stretch_wid= .1, stretch_len= .1)
    if -195< actsnow.xcor()<-205 :   #no more snow on middle line(almost)   (FIXED IT)
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


  if 160 < s1.ycor() <170:   #Hide turtle behind window bar
    s1.hideturtle()
  else:
    s1.showturtle()
  if 160 < s2.ycor() <170:
    s2.hideturtle()
  else:
    s2.showturtle()
  if 160 <s3.ycor()<170:
    s3.hideturtle()
  else:
    s3.showturtle()
  if 160 < s4.ycor() <170:
    s4.hideturtle()
  else:
    s4.showturtle()


  if s1.ycor() > 100:   #gets rid of snow below window
    snowflakes.append(s1)
  else:
    s1.hideturtle()
  if s2.ycor() > 100:
    snowflakes.append(s2)
  else:
    s2.hideturtle()
  if s3.ycor() > 100:
    snowflakes.append(s3)
  else:
    s3.hideturtle()
  if s4.ycor() > 100:
    snowflakes.append(s4)
  else:
    s4.hideturtle()
    
  
    #Second window
  if alternate%30 == 0:
    actsnow = trtl.Turtle()
    actsnow.hideturtle()
    actsnow.setheading(270)
    actsnow.penup()
    actsnow.goto(ran.randint(155, 245), 230)
    actsnow.shape('circle')
    actsnow.color('white')
    actsnow.shapesize(stretch_wid= .1, stretch_len= .1)
    secondwindow.append(actsnow)
    alternate=alternate+1
    if 195> actsnow.xcor()>205:
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
  
  


  if 160 < s1.ycor() <170:   #Hide turtle behind window bar
    s1.hideturtle()
  else:
    s1.showturtle()
  if 160 < s2.ycor() <170:
    s2.hideturtle()
  else:
    s2.showturtle()
  if 160 <s3.ycor()<170:
    s3.hideturtle()
  else:
    s3.showturtle()
  if 160 < s4.ycor() <170:
    s4.hideturtle()
  else:
    s4.showturtle()


  if s1.ycor() > 100:   #gets rid of snow below window
    secondwindow.append(s1)
  else:
    s1.hideturtle()
  if s2.ycor() > 100:
    secondwindow.append(s2)
  else:
    s2.hideturtle()
  if s3.ycor() > 100:
    secondwindow.append(s3)
  else:
    s3.hideturtle()
  if s4.ycor() > 100:
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
