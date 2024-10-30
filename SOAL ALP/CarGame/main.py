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
GREY = (100, 100, 100)
BACKGROUND_COLOR = (50, 150, 50)  # Warna jalur lintasan

# Path ke folder asset
ASSET_PATH = Path("Asset")

# Mengatur kecepatan permainan dan skor
clock = pygame.time.Clock()
FPS = 60

# Ukuran mobil dan pembagian jalur
CAR_WIDTH = 200
CAR_HEIGHT = 200
LEFT_LANE_X = (SCREEN_WIDTH // 4) - (CAR_WIDTH // 2)   # Posisi jalur kiri
RIGHT_LANE_X = (3 * SCREEN_WIDTH // 4) - (CAR_WIDTH // 2)  # Posisi jalur kanan

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
        self.color = BACKGROUND_COLOR

    def draw(self):
        screen.fill(GREY)
        
        # Gambar jalan utama
        pygame.draw.rect(screen, self.color, (LEFT_LANE_X - 70, 0, RIGHT_LANE_X - LEFT_LANE_X + CAR_WIDTH + 140, SCREEN_HEIGHT))

        # Garis tepi jalur
        pygame.draw.line(screen, WHITE, (LEFT_LANE_X - 75, 0), (LEFT_LANE_X - 75, SCREEN_HEIGHT), 5)
        pygame.draw.line(screen, WHITE, (RIGHT_LANE_X + CAR_WIDTH + 75, 0), (RIGHT_LANE_X + CAR_WIDTH + 75, SCREEN_HEIGHT), 5)
        
        # Garis putus-putus tengah
        for y in range(0, SCREEN_HEIGHT, 60):
            pygame.draw.rect(screen, WHITE, (SCREEN_WIDTH // 2 - 5, y, 10, 40))

# Kelas Player
class Player:
    def __init__(self):
        self.image = pygame.transform.scale(player_image, (CAR_WIDTH, CAR_HEIGHT))
        self.position = 'left'  # Awal di jalur kiri
        self.rect = self.image.get_rect(center=(LEFT_LANE_X, SCREEN_HEIGHT - 150))

    def move(self, direction):
        if direction == "LEFT" and self.position == 'right':
            self.rect.x = LEFT_LANE_X
            self.position = 'left'
            move_sound.play()
        elif direction == "RIGHT" and self.position == 'left':
            self.rect.x = RIGHT_LANE_X
            self.position = 'right'
            move_sound.play()

    def draw(self):
        screen.blit(self.image, self.rect)

# Kelas Enemy
class Enemy:
    def __init__(self):
        self.image = pygame.transform.scale(enemy_image, (CAR_WIDTH, CAR_HEIGHT))
        self.speed = 5
        self.reset_position()

    def reset_position(self):
        # Posisi enemy secara acak di antara dua jalur
        self.rect = self.image.get_rect(center=(
            random.choice([LEFT_LANE_X, RIGHT_LANE_X]),
            -CAR_HEIGHT
        ))

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > SCREEN_HEIGHT:
            self.reset_position()
            return True
        return False

    def increase_speed(self):
        self.speed += 0.2

    def draw(self):
        screen.blit(self.image, self.rect)

# Fungsi utama game
async def main():
    player = Player()
    enemy = Enemy()
    track = Track()
    score = 0

    # Widget skor dan judul
    score_display = pygwidgets.DisplayText(screen, (SCREEN_WIDTH // 2 - 50, 40), f"Score: {score}", fontSize=30, textColor=BLACK)
    title_display = pygwidgets.DisplayText(screen, (SCREEN_WIDTH // 2 - 70, 5), "Car Game", fontSize=40, textColor=BLACK)

    # Loop utama game
    game_over = False
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN and not game_over:
                if event.key == K_LEFT:
                    player.move("LEFT")
                elif event.key == K_RIGHT:
                    player.move("RIGHT")

        # Update layar hanya jika permainan belum berakhir
        if not game_over:
            screen.fill(GREY)
            track.draw()
            player.draw()
            enemy.draw()

            # Update posisi musuh dan skor
            if enemy.update():
                score += 10
                enemy.increase_speed()

            # Cek tabrakan
            if player.rect.colliderect(enemy.rect):
                collision_sound.play()
                pygame.mixer.music.stop()
                game_over = True
                game_over_display = pygwidgets.DisplayText(screen, (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 - 20), "Game Over!", fontSize=50, textColor=BLACK)

            # Tampilkan judul dan skor
            score_display.setValue(f"Score: {score}")
            score_display.draw()
            title_display.draw()

        # Tampilan game over
        if game_over:
            game_over_display.draw()
        
        pygame.display.update()
        await asyncio.sleep(0)
        clock.tick(FPS)

# Jalankan game
asyncio.run(main())
