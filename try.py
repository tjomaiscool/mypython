import arcade

class Circle:
    def __init__(self, x, y, r, c, xc, yc):
        self.circle_x = x
        self.circle_y = y
        self.circle_r = r
        self.circle_c = c
        self.circle_xc = xc
        self.circle_yc = yc

    def draw(self):
        arcade.draw_circle_filled(self.circle_x, self.circle_y, self.circle_r, self.circle_c)

    def update_position(self):
        # Update the circle's position
        self.circle_x += self.circle_xc
        self.circle_y += self.circle_yc

        # Check for collision with the edges of the window and reverse direction if necessary
        if self.circle_x > 700 - self.circle_r or self.circle_x < self.circle_r:
            self.circle_xc *= -1  # Reverse x direction
        if self.circle_y > 700 - self.circle_r or self.circle_y < self.circle_r:
            self.circle_yc *= -1  # Reverse y direction

class Game(arcade.Window):
    def __init__(self, w, h, t):
        super().__init__(w, h, t)
        arcade.set_background_color(arcade.color.AMBER)
        self.circle = Circle(230, 587, 34, arcade.color.AERO_BLUE, 8, 8)

    def on_draw(self):
        self.clear()
        self.circle.draw()

    def on_update(self, delta_time):
        self.circle.update_position()  # Update the circle's position and handle bouncing

def main():
    window = Game(700, 700, "Game Window")
    arcade.run()

main()
