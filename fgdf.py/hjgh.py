# game_three_paddles.py
# 3-paddle ping-pong. Switch active paddle with SPACE, move with arrows (or A/D).
import pygame
import sys
import random

# --- Config ---
WIDTH, HEIGHT = 800, 600
FPS = 60

PADDLE_W, PADDLE_H = 140, 14
PADDLE_Y = HEIGHT - 60
PADDLE_SPEED = 7

BALL_RADIUS = 10
BALL_SPEED_START = 5
BALL_SPEED_INCREMENT = 0.2  # small speed increase after paddle hit

LIVES_START = 3

# Colors (RGB)
BG = (12, 12, 20)
PADDLE_INACTIVE = (120, 120, 120)
PADDLE_ACTIVE = (0, 200, 120)
BALL_COLOR = (230, 200, 60)
TEXT_COLOR = (230, 230, 230)

# --- Init ---
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Three-Paddle Ping Pong — Switch with SPACE")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 30)
big_font = pygame.font.SysFont(None, 64)

# --- Game objects helpers ---
def clamp(val, a, b):
    return max(a, min(b, val))

class Paddle:
    def __init__(self, x):
        self.rect = pygame.Rect(x, PADDLE_Y, PADDLE_W, PADDLE_H)

    def move(self, dx):
        self.rect.x += dx
        self.rect.x = clamp(self.rect.x, 0, WIDTH - PADDLE_W)

    def draw(self, surf, is_active=False):
        color = PADDLE_ACTIVE if is_active else PADDLE_INACTIVE
        pygame.draw.rect(surf, color, self.rect, border_radius=6)

class Ball:
    def __init__(self):
        self.reset()

    def reset(self):
        self.x = WIDTH // 2
        self.y = HEIGHT // 2
        angle = random.uniform(-1.0, 1.0)  # negative -> left, positive -> right
        self.speed = BALL_SPEED_START
        self.vx = angle * self.speed
        self.vy = -self.speed  # start going upwards
        self.rect = pygame.Rect(0, 0, BALL_RADIUS*2, BALL_RADIUS*2)
        self.update_rect()

    def update_rect(self):
        self.rect.center = (int(self.x), int(self.y))

    def update(self, dt):
        self.x += self.vx * dt
        self.y += self.vy * dt
        self.update_rect()

    def draw(self, surf):
        pygame.draw.circle(surf, BALL_COLOR, (int(self.x), int(self.y)), BALL_RADIUS)

    def bounce_horizontal(self):
        self.vx = -self.vx

    def bounce_vertical(self):
        self.vy = -self.vy

# --- Game state functions ---
def draw_text_center(surf, text, y, size_font=None):
    f = size_font if size_font else font
    surf_text = f.render(text, True, TEXT_COLOR)
    rect = surf_text.get_rect(center=(WIDTH//2, y))
    surf.blit(surf_text, rect)

def start_screen():
    screen.fill(BG)
    draw_text_center(screen, "Three-Paddle Ping Pong", HEIGHT//2 - 60, big_font)
    draw_text_center(screen, "Control the ACTIVE paddle. Switch active with SPACE.", HEIGHT//2)
    draw_text_center(screen, "Move: ← → or A / D    Switch: SPACE    Pause: P    Start: ENTER", HEIGHT//2 + 40)
    draw_text_center(screen, "Press ENTER to start", HEIGHT//2 + 120)
    pygame.display.flip()

def game_over_screen(score):
    screen.fill(BG)
    draw_text_center(screen, "GAME OVER", HEIGHT//2 - 40, big_font)
    draw_text_center(screen, f"Score: {score}", HEIGHT//2 + 10)
    draw_text_center(screen, "Press ENTER to play again or ESC to quit", HEIGHT//2 + 70)
    pygame.display.flip()

# --- Main game loop ---
def run_game():
    # Create three paddles spread horizontally
    paddles = [
        Paddle(60),
        Paddle((WIDTH - PADDLE_W) // 2),
        Paddle(WIDTH - 60 - PADDLE_W)
    ]
    active = 0
    ball = Ball()
    score = 0
    lives = LIVES_START
    paused = False

    running = True
    while running:
        dt = clock.tick(FPS) / (1000 / 60.0)  # normalize to ~60 FPS units
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_SPACE:
                    # switch active paddle
                    active = (active + 1) % 3
                if event.key == pygame.K_p:
                    paused = not paused
