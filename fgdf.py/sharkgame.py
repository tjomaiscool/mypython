import pygame
import random

pygame.init()

# ===============================================================
# SETUP
# ===============================================================
WIDTH, HEIGHT = 1200, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Infinite Shark Scroller (Fixed)")

clock = pygame.time.Clock()

# ===============================================================
# COLORS
# ===============================================================
BLUE  = (0, 105, 148)
WHITE = (255, 255, 255)
RED   = (200, 50, 50)
BROWN = (139, 69, 19)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

font = pygame.font.SysFont(None, 40)

# ===============================================================
# SETTINGS
# ===============================================================
GRAVITY = 0.6
JUMP_POWER = -13
SCROLL_SPEED = 6

MIN_GAP = 200
MAX_GAP = 280

MIN_Y = 350
MAX_Y = 520

GEN_BUFFER = 1600


# ===============================================================
# SHARK
# ===============================================================
class Shark:
    def __init__(self):
        self.rect = pygame.Rect(250, 300, 50, 30)
        self.vel_y = 0

        self.on_ground = False
        self.coyote = 0
        self.jump_buffer = 0

    def handle_input(self, events):
        for e in events:
            if e.type == pygame.KEYDOWN and e.key == pygame.K_SPACE:
                self.jump_buffer = 0.12

    def apply_physics(self):
        self.vel_y += GRAVITY
        self.rect.y += self.vel_y

        if self.coyote > 0:
            self.coyote -= 1/60
        if self.jump_buffer > 0:
            self.jump_buffer -= 1/60

        if self.jump_buffer > 0 and self.coyote > 0:
            self.vel_y = JUMP_POWER
            self.jump_buffer = 0
            self.coyote = 0

    def collide_platforms(self, platforms):
        self.on_ground = False

        for p in platforms:
            if self.rect.colliderect(p.rect) and self.vel_y > 0:
                self.rect.bottom = p.rect.top
                self.vel_y = 0
                self.on_ground = True

        if self.on_ground:
            self.coyote = 0.12

    def collide_jump_pads(self, jump_pads):
        for jp in jump_pads:
            if self.rect.colliderect(jp.rect) and self.vel_y > 0:
                if self.rect.bottom - self.vel_y <= jp.rect.top:
                    self.rect.bottom = jp.rect.top
                    self.vel_y = JUMP_POWER * 1.8
                    self.coyote = 0
                    self.jump_buffer = 0

    def draw(self):
        pygame.draw.rect(screen, WHITE, self.rect)


# ===============================================================
# WORLD OBJECTS
# ===============================================================
class Platform:
    def __init__(self, x, y, w):
        self.rect = pygame.Rect(x, y, w, 20)

    def update(self):
        self.rect.x -= SCROLL_SPEED

    def draw(self):
        pygame.draw.rect(screen, BROWN, self.rect)


class Human:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 20, 30)

    def update(self):
        self.rect.x -= SCROLL_SPEED

    def draw(self):
        pygame.draw.rect(screen, RED, self.rect)


class JumpPad:
    def __init__(self, x, y, w):
        self.rect = pygame.Rect(x, y, w, 20)

    def update(self):
        self.rect.x -= SCROLL_SPEED

    def draw(self):
        pygame.draw.rect(screen, GREEN, self.rect)


# ===============================================================
# WORLD
# ===============================================================
class World:
    def __init__(self):
        self.platforms = []
        self.jump_pads = []
        self.humans = []

        self.score = 0

        self.last_x = 200
        self.last_y = 450

        self.generation_buffer = 1600

        # starting platform (guaranteed safe)
        self.platforms.append(Platform(self.last_x, self.last_y, 200))

        for _ in range(8):
            self.spawn()

    # -----------------------------------------------------------
    def spawn(self):

        gap = random.randint(200, 260)
        x = self.last_x + gap

        y = self.last_y + random.randint(-30, 30)
        y = max(350, min(520, y))

        w = random.randint(150, 200)

        # decide type
        if random.random() < 0.22:
            self.jump_pads.append(JumpPad(x, y, w))
        else:
            self.platforms.append(Platform(x, y, w))

            if random.random() < 0.5:
                self.humans.append(Human(x + 40, y - 30))

        self.last_x = x + w
        self.last_y = y

    # -----------------------------------------------------------
    def update(self):

        # move everything
        for p in self.platforms:
            p.update()

        for jp in self.jump_pads:
            jp.update()

        for h in self.humans:
            h.update()

        # cleanup
        self.platforms = [p for p in self.platforms if p.rect.right > -200]
        self.jump_pads = [jp for jp in self.jump_pads if jp.rect.right > -200]
        self.humans = [h for h in self.humans if h.rect.right > -200]

        # -------------------------------------------------------
        # FIX 1: SAFE GENERATION (NO LOOP DEADLOCK)
        # -------------------------------------------------------
        # Instead of recomputing furthest, we use last_x ONLY
        while self.last_x < self.generation_buffer:
            self.spawn()

        # -------------------------------------------------------
        # SAFETY: prevent empty world collapse
        # -------------------------------------------------------
        if len(self.platforms) < 3:
            for _ in range(3):
                self.spawn()

    # -----------------------------------------------------------
    def check_eating(self, shark):
        for h in self.humans[:]:
            if shark.rect.colliderect(h.rect):
                self.humans.remove(h)
                self.score += 1

    # -----------------------------------------------------------
    def draw(self):

        for p in self.platforms:
            p.draw()

        for jp in self.jump_pads:
            jp.draw()

        for h in self.humans:
            h.draw()

        txt = font.render(f"Score: {self.score}", True, WHITE)
        screen.blit(txt, (20, 20))


# ===============================================================
# GAME LOOP
# ===============================================================
shark = Shark()
world = World()

game_over = False

running = True
while running:

    clock.tick(60)
    events = pygame.event.get()

    for e in events:
        if e.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if not game_over:

        shark.handle_input(events)
        shark.apply_physics()

        shark.collide_platforms(world.platforms)
        shark.collide_jump_pads(world.jump_pads)

        world.check_eating(shark)
        world.update()

        if shark.rect.top > HEIGHT:
            game_over = True

        screen.fill(BLUE)
        world.draw()
        shark.draw()

    else:

        screen.fill(BLACK)

        over = font.render("GAME OVER", True, WHITE)
        screen.blit(over, (520, 300))

        score = font.render(f"Final Score: {world.score}", True, WHITE)
        screen.blit(score, (500, 360))

        restart = font.render("Press R to restart", True, WHITE)
        screen.blit(restart, (450, 420))

        if keys[pygame.K_r]:
            shark = Shark()
            world = World()
            game_over = False

    pygame.display.flip()

pygame.quit()