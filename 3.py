import arcade

class Game(arcade.Window):
    def __init__(self, w, h, t):
        super().__init__(w, h, t)
        self.circle_x = 70
        self.circle_y = 70
        arcade.set_background_color(arcade.color.AMBER)
        arcade.schedule(self.update_and_draw, 1/60)

    def update_and_draw(self, delta_time: float):
            self.circle_x += 8 
            self.circle_y += 5
            self.clear()
            arcade.draw_circle_filled(self.circle_x, self.circle_y, 20, arcade.color.AIR_FORCE_BLUE)


def main():
    window = Game(700, 700, "Game Window")
    arcade.run()

main()
