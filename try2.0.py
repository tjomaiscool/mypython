import arcade

class Circle:
    def __init__(self, x, y, r, c):
        self.circle_x = x  # X position of the circle
        self.circle_y = y  # Y position of the circle
        self.circle_r = r  # Radius of the circle
        self.circle_c = c  # Color of the circle
        # Velocity for x and y directions to control speed and direction
        self.velocity_x = 8
        self.velocity_y = 8

    def draw(self):
        # Draw the circle with current position, radius, and color
        arcade.draw_circle_filled(self.circle_x, self.circle_y, self.circle_r, self.circle_c)

    def update_position(self, screen_width, screen_height):
        # Update the circle's position by adding the velocity to x and y coordinates
        self.circle_x += self.velocity_x
        self.circle_y += self.velocity_y

        # Check for bounce on the left or right edges
        if self.circle_x - self.circle_r <= 0 or self.circle_x + self.circle_r >= screen_width:
            self.velocity_x *= -1  # Reverse x direction on bounce

        # Check for bounce on the top or bottom edges
        if self.circle_y - self.circle_r <= 0 or self.circle_y + self.circle_r >= screen_height:
            self.velocity_y *= -1  # Reverse y direction on bounce


class Game(arcade.Window):
    def __init__(self, w, h, t):
        # Initialize the game window with specified width, height, and title
        super().__init__(w, h, t)
        arcade.set_background_color(arcade.color.AMBER)
        # Initialize the circle with starting position, radius, and color
        self.circle = Circle(230, 587, 34, arcade.color.AERO_BLUE)

    def on_draw(self):
        # Clear the screen and draw the circle
        self.clear()
        self.circle.draw()

    def update(self, delta_time):
        # Update the circle's position and handle bouncing
        self.circle.update_position(self.width, self.height)


def main():
    # Set up and run the game
    window = Game(700, 700, "Bouncing Circle Game")
    arcade.run()

main()
