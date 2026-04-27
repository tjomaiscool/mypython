import arcade
import random
import os

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
FALLING_BALL_RADIUS = 20
CONTROLLED_BALL_RADIUS = 40
DEFAULT_CIRCLE_SPEED = 4
DEFAULT_MOVE_SPEED = 6
TEXT_COLOR = arcade.color.WHITE
TEXT_SIZE = 20
DEFAULT_FAILS_TO_GAME_OVER = 3

class FallingBallGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Falling Ball with Score")
        self.falling_ball_x = random.randint(FALLING_BALL_RADIUS, SCREEN_WIDTH - FALLING_BALL_RADIUS)
        self.falling_ball_y = SCREEN_HEIGHT
        self.controlled_ball_x = 250
        self.controlled_ball_y = 100
        self.move_left = False
        self.move_right = False
        self.score = 0
        self.fail = 0
        self.move_speed = DEFAULT_MOVE_SPEED
        self.circle_speed = DEFAULT_CIRCLE_SPEED
        self.fails_to_game_over = DEFAULT_FAILS_TO_GAME_OVER
        self.load_config()
        
        self.endgame = False

    def load_config(self):
        if os.path.exists('python.txt'):
            with open('python.txt', 'r') as file:
                self.config_strings = file.readlines()

            self.highscore = int(self.config_strings[0].strip().replace("highscore", ""))
            self.difficulty = int(self.config_strings[1].strip().replace("difficulty", ""))

            self.config_strings = [(self.highscore), f"difficulty {self.difficulty}"]

            if self.difficulty == 2:
                self.circle_speed = 10
                self.fails_to_game_over = 2
            elif self.difficulty == 3:
                self.fails_to_game_over = 0
                self.circle_speed = 12
                self.move_speed = 15
        else:
            self.highscore = 0
            self.config_strings = ['0', '1']
            with open('python.txt', 'w') as file:
                for string in self.config_strings:
                    file.write(string + '\n')

    def on_draw(self):
        self.clear()
        if not self.endgame:
            arcade.draw_circle_filled(self.falling_ball_x, self.falling_ball_y, FALLING_BALL_RADIUS, arcade.color.AERO_BLUE)
            arcade.draw_circle_filled(self.controlled_ball_x, self.controlled_ball_y, CONTROLLED_BALL_RADIUS, arcade.color.RED)
        else:
            arcade.draw_text("Game Over", 30, SCREEN_HEIGHT // 2, arcade.color.RED, 70)
            arcade.draw_text("Press Enter to Restart", 30, SCREEN_HEIGHT // 2 - 30, arcade.color.WHITE, 20)
        arcade.draw_text(f"Score: {self.score}", 10, SCREEN_HEIGHT - 30, TEXT_COLOR, TEXT_SIZE)
        arcade.draw_text(f"Fails: {self.fail}", 10, SCREEN_HEIGHT - 60, TEXT_COLOR, TEXT_SIZE)
        arcade.draw_text(f"Highscore: {self.highscore}", 10, SCREEN_HEIGHT - 100, TEXT_COLOR, TEXT_SIZE)

    def gameover(self):
        self.fail = 0
        self.score = 0
        self.endgame = True

    def on_update(self, delta_time):
        if not self.endgame:
            self.falling_ball_y -= self.circle_speed
            if self.falling_ball_y - FALLING_BALL_RADIUS <= 0:
                self.reset_falling_ball()
                self.fail += 1
                if self.fail >= self.fails_to_game_over:
                    self.gameover()
            if self.check_collision():
                self.reset_falling_ball()
                self.score += 1
                if self.score > self.highscore:
                    self.highscore = self.score
                    
                    self.config_strings[0] = "highscore " + str(self.highscore)
                    with open('python.txt', 'w') as file:
                        for string in self.config_strings:
                            file.write(string + '\n')
            if self.move_right:
                self.controlled_ball_x += self.move_speed
            if self.move_left:
                self.controlled_ball_x -= self.move_speed
            self.controlled_ball_x = max(CONTROLLED_BALL_RADIUS, min(SCREEN_WIDTH - CONTROLLED_BALL_RADIUS, self.controlled_ball_x))

    def on_key_press(self, key, modifiers):
        if key == arcade.key.D:
            self.move_right = True
        elif key == arcade.key.A:
            self.move_left = True
        elif key == arcade.key.ENTER:
            self.endgame = False
            self.score = 0
            self.fail = 0
            self.reset_falling_ball()

    def on_key_release(self, key, modifiers):
        if key == arcade.key.D:
            self.move_right = False
        elif key == arcade.key.A:
            self.move_left = False

    def check_collision(self):
        return (abs(self.falling_ball_x - self.controlled_ball_x) < FALLING_BALL_RADIUS + CONTROLLED_BALL_RADIUS and
                abs(self.falling_ball_y - self.controlled_ball_y) < FALLING_BALL_RADIUS + CONTROLLED_BALL_RADIUS)

    def reset_falling_ball(self):
        self.falling_ball_x = random.randint(FALLING_BALL_RADIUS, SCREEN_WIDTH - FALLING_BALL_RADIUS)
        self.falling_ball_y = SCREEN_HEIGHT

def main():
    FallingBallGame().run()

if __name__ == "__main__":
    main()
