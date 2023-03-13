""" Lab 7 - User Control """

import arcade
import background


# --- Constants ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class Sun:
    def __init__(self, position_x, position_y, radius, color):
        self.position_x = position_x
        self.position_y = position_y
        self.radius = radius
        self.color = color

    def draw(self):

        arcade.draw_circle_filled(self.position_x, self.position_y, self.radius, self.color)
        background.sun(self.position_x, self.position_y)


class MyGame(arcade.Window):
    """ Our Custom Window Class"""

    def __init__(self):
        """ Initializer """

        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Lab 7 - User Control")

        # make the cursor invisible
        self.set_mouse_visible(False)

        # draw the Sun
        self.Sun = Sun(50,50, 18, arcade.color.RED)

    def on_draw(self):
        arcade.start_render()
        arcade.set_background_color(arcade.color.WHITE)

        # draw the background
        background.draw()

        self.Sun.draw()

    def on_mouse_motion(self, x, y, dx, dy):

        self.Sun.position_x = x
        self.Sun.position_y = y

def main():
    window = MyGame()
    arcade.run()


main()