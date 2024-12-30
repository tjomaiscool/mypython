import arcade
window = arcade.open_window(500,500,"gvfgv", resizable=False)
arcade.set_background_color(arcade.color.AERO_BLUE)
arcade.start_render()
arcade.draw_lrbt_rectangle_filled(0, 500, 0,75, arcade.color.ELECTRIC_LIME)
arcade.draw_lrbt_rectangle_filled(200, 400, 75,125, arcade.color.BROWN)
arcade.draw_triangle_filled(200,125,400,125 ,300,175,arcade.color.LIGHT_BROWN)
arcade.finish_render()
arcade.run()