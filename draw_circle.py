import arcade

def drawCircle():
    window = arcade.open_window(500,500,"gvfgv", resizable=True)
    arcade.set_background_color(arcade.color.AERO_BLUE)


    arcade.start_render()
    arcade.draw_circle_filled(200,200,100,arcade.color.RACKLEY)
    arcade.finish_render()
    arcade.run()