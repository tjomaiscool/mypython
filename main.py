import arcade


def sun(x, y):
    arcade.draw_circle_filled(-17.5 + x, -17.5 + y, 35, arcade.color.RED)

def ground():
    arcade.draw_lrbt_rectangle_filled(0, 500, 0, 75, arcade.color.GREEN)

def tree(x):
    arcade.draw_lbwh_rectangle_filled(-12.5 + x, 75, 25, 80, arcade.color.BROWN)
    arcade.draw_circle_filled(0 + x, 150, 25, arcade.color.GREEN)

def draw(time):
    arcade.get_window().clear()  # Clear the screen instead of start_render()
    ground()
    tree(300)
    tree(200)
    tree(100)
    sun(draw.sun_x, 400)  # Adjust the sun's initial y position
    #arcade.finish_render()  # Moved this here
    draw.sun_x -= 1  # Move the sun left by 1 pixel per frame


    

def main():
    arcade.open_window(500, 500, "window")
    arcade.set_background_color(arcade.color.SKY_BLUE)
    

    draw.sun_x = 500

    arcade.schedule(draw, 1/60)


    #draw(1)
    arcade.run()

main()
      
 