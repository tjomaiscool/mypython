import arcade  
window = arcade.open_window(500,500,"gvfgv", resizable=True)
arcade.set_background_color(arcade.color.AERO_BLUE)
arcade.start_render()
arcade.draw_text("bla",10,100,arcade.color.YELLOW,20,400)
arcade.finish_render()
arcade.run()