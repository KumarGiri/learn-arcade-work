import arcade
import math
import random

HEIGHT = 600
WIDTH = 1000

arcade.open_window(WIDTH, HEIGHT, "Draw Using functions")
arcade.set_background_color(arcade.color.WHITE)
arcade.start_render()

#cloud function
def cloud_ovals(x_center, y_center):
    arcade.draw_ellipse_filled(x_center, y_center, width=50, height=30, color=arcade.color.ASH_GREY)

# function for a sigle cloud
def cloud(x_center, y_center):
     cloud_ovals(x_center, y_center)
     cloud_ovals(x_center+25, y_center)
     cloud_ovals(x_center+25, y_center+10)

# placing clouds into specific locations
cloud(random.randint(100,1000), 500)
cloud(300, random.randint(400,550))
cloud(random.randint(100,1000), 520)

#Tree leaf
arcade.draw_line(650, 600, 625, 450, color=arcade.color.WARM_BLACK)
def leafs(x_center, y_center, tangle):
    return arcade.draw_ellipse_filled(x_center, y_center, 50, 10, color=arcade.color.WARM_BLACK, tilt_angle=tangle)
leafs(628, 450,90)
leafs(650, 475, 45)
leafs(612, 475, 135)

x_center= 650
y_center= 475
for x in range (1,8):
    x_center +=3
    y_center +=18
    leafs(x_center, y_center, random.randint(15,45))
x_center= 612
y_center= 475
for x in range (1,8):
    x_center +=2
    y_center +=18
    leafs(x_center, y_center, random.randint(135,155))


#sun reflection function
def sun_reflect(num_lines):
    startx=550 
    starty=290
    endx= 650
    endy=290

    for x in range (0, num_lines):
         startx-=10
         endx+=10
         starty-=20
         endy-=20
         arcade.draw_line(startx,starty, endx, endy, color=arcade.color.RED_ORANGE )
sun_reflect(6)

arcade.finish_render()

arcade.run()