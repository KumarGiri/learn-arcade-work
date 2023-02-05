import arcade
import math
import random

#cloud function
def cloud_ovals(x_center, y_center):
    arcade.draw_ellipse_filled(x_center, y_center, width=50, height=30, color=arcade.color.ASH_GREY)

# function for a sigle cloud
def cloud(x_center, y_center):
     cloud_ovals(x_center, y_center)
     cloud_ovals(x_center+25, y_center)
     cloud_ovals(x_center+25, y_center+10)

def cloud_cousters(x):
    cloud(800+x, 500)
    cloud(300+x, 550)
    cloud(400+x, 520)


# leaves
def leafs(x_center, y_center, tangle):
    return arcade.draw_ellipse_filled(x_center, y_center, 50, 10, color=arcade.color.WARM_BLACK, tilt_angle=tangle)
# drawing leaves around the branch
def individual_leaves():
    x_center= 650
    y_center= 475
    for x in range (1,8):
        x_center +=3
        y_center +=18
        leafs(x_center, y_center, 30)
    x_center= 612
    y_center= 475
    for x in range (1,8):
        x_center +=2
        y_center +=18
        leafs(x_center, y_center, 145)


# draw sun and its rays
def sun(sx, sy, radius):
    for j in range(0,360, 40):
        arcade.draw_line(sx+50*math.sin(math.radians(j)), sy+50*math.cos(math.radians(j)), sx+30*math.sin(math.radians(j)), sy+30*math.cos(math.radians(j)), arcade.color.SUNRAY, 2)
        for j in range(20,380, 40):
            arcade.draw_line(sx+45*math.sin(math.radians(j)), sy+45*math.cos(math.radians(j)), sx+30*math.sin(math.radians(j)), sy+30*math.cos(math.radians(j)), arcade.color.SUNRAY, 2)
    arcade.draw_circle_filled(sx, sy, radius, arcade.color.SUNGLOW)

# draw birds
def bird(x, ystart):
    arcade.draw_arc_outline(x, ystart, 15, 15, arcade.color.BLACK, 0, 155, 4)
    arcade.draw_arc_outline(x+14, ystart, 15, 15, arcade.color.BLACK, 35, 180, 4)
