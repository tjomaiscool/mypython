import arcade

class Game(arcade.Window):
    def __init__(self, w, h, t):
        super().__init__(w, h, t)
        arcade.set_background_color(arcade.color.AMBER)
        arcade.start_render()

def main():
    window = Game(700, 700, "Game Window")
    arcade.run()

main()

 