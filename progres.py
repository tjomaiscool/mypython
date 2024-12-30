import arcade
import arcade.draw

window = arcade.open_window(500,500, "name")
arcade.set_background_color(arcade.color.AERO_BLUE)
arcade.start_render()
arcade.draw_lines(((0 , 500),(500 , 0),(500,500),(0,0)) ,arcade.color.TANGERINE_YELLOW)

arcade.finish_render()
arcade.run()
