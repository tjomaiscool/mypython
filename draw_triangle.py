import arcade

def drawtriangle():
    window = arcade.open_window(500,500,"gvfgv", resizable=True)
    arcade.set_background_color(arcade.color.AERO_BLUE)


    arcade.start_render()
    arcade.draw_triangle_filled(5,5,50,60,100,5,arcade.color.RACKLEY)
    arcade.finish_render()
    arcade.run()
drawtriangle()