import arcade
import random

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
FALLING_BALL_RADIUS = 20
CONTROLLED_BALL_RADIUS = 40
CIRCLE_SPEED = 4
MOVE_SPEED = 6
TEXT_COLOR = arcade.color.WHITE
TEXT_SIZE = 20
FAILS_TO_GAME_OVER = 3

class FallingBallGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Falling Ball with Score")
        self.falling_ball_x = random.randint(FALLING_BALL_RADIUS, SCREEN_WIDTH - FALLING_BALL_RADIUS)
        self.falling_ball_y = SCREEN_HEIGHT
        self.controlled_ball_x = 250
        self.controlled_ball_y = 100
        self.move_left = False
        self.move_right = False
        self.score = 0  # Initialize the score to 0
        self.fail = 0  # Initialize the fail count to 0
        self.highscore = 0
        self.endgame = False

    def on_draw(self):
        self.clear()
        if self.endgame == False:
            # Draw the falling ball
            arcade.draw_circle_filled(self.falling_ball_x, self.falling_ball_y, FALLING_BALL_RADIUS, arcade.color.AERO_BLUE)
            # Draw the controlled ball
            arcade.draw_circle_filled(self.controlled_ball_x, self.controlled_ball_y, CONTROLLED_BALL_RADIUS, arcade.color.RED)
        else:
            arcade.draw_text("Game Over", 30, SCREEN_HEIGHT // 2, arcade.color.RED, 70)
            arcade.draw_text("Press Enter to Restart", 30, SCREEN_HEIGHT // 2 - 30, arcade.color.WHITE, 20)
        # Draw the score and fail count on the screen
        arcade.draw_text(f"Score: {self.score}", 10, SCREEN_HEIGHT - 30, TEXT_COLOR, TEXT_SIZE)
        arcade.draw_text(f"Fails: {self.fail}", 10, SCREEN_HEIGHT - 60, TEXT_COLOR, TEXT_SIZE)
        arcade.draw_text(f"Highscore: {self.highscore}", 10, SCREEN_HEIGHT - 100, TEXT_COLOR, TEXT_SIZE)

    def gameover(self):
        self.fail = 0
        self.score = 0
        self.endgame = True

    def on_update(self, delta_time):
        if self.endgame == False:
            # Falling ball logic
            self.falling_ball_y -= CIRCLE_SPEED

            # Reset if the falling ball hits the bottom of the screen
            if self.falling_ball_y - FALLING_BALL_RADIUS <= 0:
                self.reset_falling_ball()
                self.fail += 1  # Increment the fail count when the ball is missed
                if self.fail >= FAILS_TO_GAME_OVER:
                    self.gameover()  # Trigger game over when fails exceed limit
            # Reset if the falling ball overlaps the controlled ball and increase the score
            if self.check_collision():
                self.reset_falling_ball()
                self.score += 1  # Increase the score on collision
                if self.score > self.highscore:
                    self.highscore = self.score
            # Controlled ball logic
            if self.move_right:
                self.controlled_ball_x += MOVE_SPEED
            if self.move_left:
                self.controlled_ball_x -= MOVE_SPEED

            # Keep the controlled ball within screen boundaries
            self.controlled_ball_x = max(CONTROLLED_BALL_RADIUS, min(SCREEN_WIDTH - CONTROLLED_BALL_RADIUS, self.controlled_ball_x))

    def on_key_press(self, key, modifiers):
        if key == arcade.key.D:
            self.move_right = True
        elif key == arcade.key.A:
            self.move_left = True
        elif key == arcade.key.ENTER:
            self.endgame = False

    def on_key_release(self, key, modifiers):
        if key == arcade.key.D:
            self.move_right = False
        elif key == arcade.key.A:
            self.move_left = False

    def reset_falling_ball(self):
        # Reset the falling ball to the top at a random x position
        self.falling_ball_x = random.randint(FALLING_BALL_RADIUS, SCREEN_WIDTH - FALLING_BALL_RADIUS)
        self.falling_ball_y = SCREEN_HEIGHT

    def check_collision(self):
        # Check if the falling ball overlaps the controlled ball
        return (abs(self.falling_ball_x - self.controlled_ball_x) < FALLING_BALL_RADIUS + CONTROLLED_BALL_RADIUS and
                abs(self.falling_ball_y - self.controlled_ball_y) < FALLING_BALL_RADIUS + CONTROLLED_BALL_RADIUS)


def main():
    FallingBallGame().run()

if __name__ == "__main__":
    main()
