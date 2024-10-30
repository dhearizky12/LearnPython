import pygame, sys, random, pygwidgets, asyncio
from pygame.locals import *
from pathlib import Path

# Inisialisasi pygame
pygame.init()

# Ukuran layar
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 700
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Car Game")

# Warna dan Asset
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BACKGROUND_COLOR = (50, 150, 50)  # Warna jalur lintasan

# Path ke folder asset
ASSET_PATH = Path("Asset")

# Mengatur kecepatan permainan dan skor
clock = pygame.time.Clock()
FPS = 60

# Asset mobil dan suara
player_image = pygame.image.load(ASSET_PATH / "player_car.png")
enemy_image = pygame.image.load(ASSET_PATH / "enemy_car.png")
pygame.mixer.music.load(ASSET_PATH / "background_music.wav")
pygame.mixer.music.play(-1)
collision_sound = pygame.mixer.Sound(ASSET_PATH / "collision.wav")
move_sound = pygame.mixer.Sound(ASSET_PATH / "move.wav")

# Kelas Track (Lintasan)
class Track:
    def __init__(self):
        self.x = 150
        self.width = 300
        self.color = BACKGROUND_COLOR

    def draw(self):
        screen.fill(WHITE)
        pygame.draw.rect(screen, self.color, (self.x, 0, self.width, SCREEN_HEIGHT))

# Kelas Player
class Player:
    def __init__(self):
        self.image = pygame.transform.scale(player_image, (50, 100))
        self.rect = self.image.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 120))
        self.speed = 5

    def move(self, direction):
        if direction == "LEFT" and self.rect.left > 150:
            self.rect.x -= self.speed
            move_sound.play()
        elif direction == "RIGHT" and self.rect.right < 450:
            self.rect.x += self.speed
            move_sound.play()

    def draw(self):
        screen.blit(self.image, self.rect)

# Kelas Enemy
class Enemy:
    def __init__(self):
        self.image = pygame.transform.scale(enemy_image, (50, 100))
        self.rect = self.image.get_rect(center=(random.randint(200, 400), -100))
        self.speed = 5

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > SCREEN_HEIGHT:
            self.rect.center = (random.randint(200, 400), -100)
            return True
        return False

    def increase_speed(self):
        self.speed += 0.5

    def draw(self):
        screen.blit(self.image, self.rect)

# Fungsi utama game
async def main():
    player = Player()
    enemy = Enemy()
    track = Track()
    score = 0

    # Widget skor dan judul
    score_display = pygwidgets.DisplayText(screen, (50, 10), f"Score: {score}", fontSize=30, textColor=BLACK)
    title_display = pygwidgets.DisplayText(screen, (SCREEN_WIDTH // 2 - 70, 10), "Car Game", fontSize=40, textColor=BLACK)

    # Loop utama game
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_LEFT:
                    player.move("LEFT")
                elif event.key == K_RIGHT:
                    player.move("RIGHT")

        # Update
        screen.fill(WHITE)
        track.draw()
        player.draw()
        enemy.draw()

        if enemy.update():  # Jika enemy melewati layar
            score += 10
            enemy.increase_speed()

        # Cek tabrakan
        if player.rect.colliderect(enemy.rect):
            collision_sound.play()
            pygame.mixer.music.stop()
            pygame.time.delay(1000)
            pygame.quit()
            sys.exit()

        # Tampilkan judul dan skor
        score_display.setValue(f"Score: {score}")
        score_display.draw()
        title_display.draw()

        pygame.display.update()
        await asyncio.sleep(0)
        clock.tick(FPS)

# Jalankan game
asyncio.run(main())
