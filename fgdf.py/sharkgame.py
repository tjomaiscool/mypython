import pygame
import random

pygame.init()

# ===============================================================
# SETUP
# ===============================================================

WIDTH, HEIGHT = 1200, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Infinite Shark Scroller")

clock = pygame.time.Clock()

# Colors
BLUE = (0, 105, 148)
WHITE = (255, 255, 255)
RED = (200, 50, 50)
BROWN = (139, 69, 19)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

font = pygame.font.SysFont(None, 40)

# Physics
GRAVITY = 0.6
JUMP_POWER = -13
SCROLL_SPEED = 10    # ← BASE SPEED (per 60 FPS)

# ===============================================================
# SHARK — Jump buffer + coyote time + continuous collision
# ===============================================================

class Shark:
    def __init__(self):
        self.rect = pygame.Rect(250, 300, 50, 30)
        self.vel_y = 0
        self.on_ground = False

        # Helpers
        self.coyote_timer = 0
        self.jump_buffer = 0

    def press_jump(self):
        self.jump_buffer = 0.15  # buffered jump

    def update(self, platforms, jump_pads, dt):
        # Apply gravity
        self.vel_y += GRAVITY * dt

        # Update timers
        if self.coyote_timer > 0:
            self.coyote_timer -= dt
        if self.jump_buffer > 0:
            self.jump_buffer -= dt

        # Vertical movement split into steps
        steps = max(1, int(abs(self.vel_y)))
        step = self.vel_y / steps

        self.on_ground = False

        for _ in range(steps):
            self.rect.y += step

            # PLATFORM COLLISION
            for p in platforms:
                if self.rect.colliderect(p.rect) and step > 0:
                    self.rect.bottom = p.rect.top
                    self.vel_y = 0
                    self.on_ground = True
                    self.coyote_timer = 0.15
                    break

            # JUMP PAD COLLISION
            for jp in jump_pads:
                if (
                    self.rect.colliderect(jp.rect)
                    and step > 0
                    and self.rect.bottom <= jp.rect.top + 12
                ):
                    self.rect.bottom = jp.rect.top
                    self.vel_y = JUMP_POWER * 1.8
                    self.on_ground = False
                    self.coyote_timer = 0
                    self.jump_buffer = 0
                    return  # exit early; giant boost

        # EXECUTE JUMP IF POSSIBLE
        if self.jump_buffer > 0 and self.coyote_timer > 0:
            self.vel_y = JUMP_POWER
            self.jump_buffer = 0
            self.coyote_timer = 0

    def draw(self):
        pygame.draw.rect(screen, WHITE, self.rect)

# ===============================================================
# OBJECTS
# ===============================================================

class Platform:
    def __init__(self, x, y, w):
        self.rect = pygame.Rect(x, y, w, 20)

    def update(self, dt):
        self.rect.x -= SCROLL_SPEED * dt

    def draw(self):
        pygame.draw.rect(screen, BROWN, self.rect)


class JumpPad:
    def __init__(self, x, y, w):
        self.rect = pygame.Rect(x, y, w, 20)

    def update(self, dt):
        self.rect.x -= SCROLL_SPEED * dt

    def draw(self):
        pygame.draw.rect(screen, GREEN, self.rect)


class Human:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 20, 30)

    def update(self, dt):
        self.rect.x -= SCROLL_SPEED * dt

    def draw(self):
        pygame.draw.rect(screen, RED, self.rect)

# ===============================================================
# WORLD — Fake delta-time + stable generation
# ===============================================================

class World:
    def __init__(self):
        self.platforms = []
        self.jump_pads = []
        self.humans = []

        self.score = 0

        self.last_x = 200
        self.last_y = 450

        # Start base platform
        self.platforms.append(Platform(200, 450, 250))

        # Pre-generate
        for _ in range(10):
            self.spawn()

    def spawn(self):
        # Basic platform spacing
        gap = random.randint(260, 360)
        x = self.last_x + gap
        y = self.last_y + random.randint(-40, 40)
        y = max(320, min(560, y))
        w = random.randint(140, 200)

        roll = random.random()

        if roll < 0.25:
            # Jump pad
            self.jump_pads.append(JumpPad(x, y, w))

            # NEXT PLATFORM must be safe
            safe_gap = random.randint(240, 300)
            nx = x + w + safe_gap
            ny = y + random.randint(-30, 30)
            ny = max(320, min(560, ny))
            nw = random.randint(280, 340)

            self.platforms.append(Platform(nx, ny, nw))
            self.last_x = nx + nw
            self.last_y = ny

        else:
            # Normal platform
            self.platforms.append(Platform(x, y, w))
            if random.random() < 0.4:
                self.humans.append(Human(x + 40, y - 30))

            self.last_x = x + w
            self.last_y = y

    def update(self, dt):
        # Scroll all objects
        for p in self.platforms:
            p.update(dt)
        for jp in self.jump_pads:
            jp.update(dt)
        for h in self.humans:
            h.update(dt)

        # Cleanup
        self.platforms = [p for p in self.platforms if p.rect.right > -500]
        self.jump_pads = [jp for jp in self.jump_pads if jp.rect.right > -500]
        self.humans = [h for h in self.humans if h.rect.right > -500]

        # Generate forward
        camera_right = 250 + WIDTH
        while self.last_x < camera_right + 900:
            self.spawn()

        # Safety platforms
        if len(self.platforms) < 5:
            for _ in range(5):
                self.spawn()

    def check_eating(self, shark):
        for h in self.humans[:]:
            if shark.rect.colliderect(h.rect):
                self.humans.remove(h)
                self.score += 1

    def draw(self):
        for p in self.platforms:
            p.draw()
        for jp in self.jump_pads:
            jp.draw()
        for h in self.humans:
            h.draw()

        # Score
        t = font.render(f"Score: {self.score}", True, WHITE)
        screen.blit(t, (20, 20))

# ===============================================================
# GAME LOOP
# ===============================================================

shark = Shark()
world = World()

running = True
game_over = False

while running:
    dt = clock.tick(60) / 16.666   # FAKE DELTA (1.0 = 60 FPS)

    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            shark.press_jump()

    if not game_over:
        shark.update(world.platforms, world.jump_pads, dt)
        world.update(dt)
        world.check_eating(shark)

        if shark.rect.top > HEIGHT:
            game_over = True

        screen.fill(BLUE)
        world.draw()
        shark.draw()

    else:
        screen.fill(BLACK)

        over = font.render("GAME OVER", True, WHITE)
        screen.blit(over, (520, 300))

        final_score = font.render(f"Final Score: {world.score}", True, WHITE)
        screen.blit(final_score, (500, 350))

        restart = font.render("Press R to Restart", True, WHITE)
        screen.blit(restart, (460, 400))

        if keys[pygame.K_r]:
            shark = Shark()
            world = World()
            game_over = False

    pygame.display.flip()

pygame.quit()