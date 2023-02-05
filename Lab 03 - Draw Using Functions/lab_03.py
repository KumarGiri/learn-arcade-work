import arcade

HEIGHT = 600
WIDTH = 800

# draw hills
def hills(x_center, y_center, length, height, startangle, endangle):
    arcade.draw_arc_filled(x_center, y_center, length, height, arcade.color.GREEN, start_angle=startangle, end_angle=endangle)

#Tree leaf
def branch():
    arcade.draw_line(647, 600, 625, 450, color=arcade.color.WARM_BLACK)

# draw everything
def on_draw(deltatime):
    arcade.start_render()
    import custom_library as cl

    cl.sun(on_draw.x/2+200, 530-on_draw.x/3, 30)
   
    cl.cloud_cousters(on_draw.x)

    # draw birds    
    cl.bird(on_draw.x/3+200, on_draw.x/10+400)
    cl.bird(on_draw.x/2+220, on_draw.x/10+400)

    hills(0, 0, 700, 400, 0, 90)
    hills(800, 0, 600, 500, 90, 180 )
    hills(500, 0, 400, 300, 0, 180)

    # draw leaves
    branch()
    cl.leafs(628, 450,90)
    cl.leafs(650, 475, 45)
    cl.leafs(612, 475, 135)
    cl.individual_leaves()

    on_draw.x += 1

    arcade.finish_render()
on_draw.x = 0


# main function
def main():
    arcade.open_window(WIDTH, HEIGHT, "Draw Using functions")
    arcade.set_background_color(arcade.color.SKY_BLUE)
    arcade.schedule(on_draw, 1/30)
    arcade.run()

# call main function    
main()