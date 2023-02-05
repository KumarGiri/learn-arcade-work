import arcade

HEIGHT = 600
WIDTH = 1000
background_texture= arcade.load_texture("Jon Kleinberg.png")
 
# draw window
def structures():
    arcade.draw_lrtb_rectangle_filled(50, 950, 598, 299, arcade.color.SKY_BLUE)
    arcade.draw_lrtb_rectangle_outline(51, 951, 600, 300, arcade.color.BLACK, 3)
    arcade.draw_lrwh_rectangle_textured(0, 0, 1000, 400, background_texture)

#Tree leaf
def branch():
    arcade.draw_line(650, 600, 625, 450, color=arcade.color.WARM_BLACK)

# draw everything
def on_draw(deltatime):
    arcade.start_render()
    structures()
    import custom_library as cl
    cl.cloud_cousters(on_draw.x)

    # draw birds    
    cl.bird(on_draw.x/3+200, on_draw.x/10+400)
    cl.bird(on_draw.x/2+220, on_draw.x/10+400)

    # draw leaves
    branch()
    cl.leafs(628, 450,90)
    cl.leafs(650, 475, 45)
    cl.leafs(612, 475, 135)
    cl.individual_leaves()

    cl.sun(200, 530, 30)
    on_draw.x += 1

    arcade.finish_render()
on_draw.x = 0


# main function
def main():
    arcade.open_window(WIDTH, HEIGHT, "Draw Using functions")
    arcade.set_background_color(arcade.color.WHITE)
    arcade.schedule(on_draw, 1/60)
    arcade.run()

# call main function    
main()