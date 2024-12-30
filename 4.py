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

    def update(self):  # Renamed to update
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

        self.circle_list = []
        # Add circles to the list
        self.circle_list.append(Circle(230, 587, 34, arcade.color.AERO_BLUE, 8, 8))
        self.circle_list.append(Circle(60, 560, 57, arcade.color.AERO_BLUE, 8, 8))
        self.circle_list.append(Circle(590, 444, 100, arcade.color.AERO_BLUE, 8, 8))

    def on_draw(self):
        self.clear()
        for c in self.circle_list:
            c.draw()

    def on_update(self, delta_time):
        for c in self.circle_list:
            c.update()  # Now this calls the update method of each circle

def main():
    window = Game(700, 700, "Game Window")
    arcade.run()

main()
