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
GREEN = (76, 208, 56)
YELLOW = (255, 232, 0)

# Path ke folder asset
ASSET_PATH = Path("Asset")

# Pengaturan permainan
FPS = 60
clock = pygame.time.Clock()
CAR_WIDTH = 140
CAR_HEIGHT = 140
LEFT_LANE_X = SCREEN_WIDTH // 4 - CAR_WIDTH // 2
RIGHT_LANE_X = 3 * SCREEN_WIDTH // 4 - CAR_WIDTH // 2
lane_marker_move_y = 0
score = 0
speed = 5
game_over = False
last_lane = None  # Untuk menyimpan posisi terakhir enemy

# Load gambar dan suara
player_image = pygame.image.load(ASSET_PATH / "player_car.png")
enemy_image = pygame.image.load(ASSET_PATH / "enemy_car.png")
crash_image = pygame.image.load(ASSET_PATH / "crash.png")
pygame.mixer.music.load(ASSET_PATH / "background_music.wav")
pygame.mixer.music.play(-1)
collision_sound = pygame.mixer.Sound(ASSET_PATH / "collision.wav")
move_sound = pygame.mixer.Sound(ASSET_PATH / "move.wav")

# Kelas Player
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(player_image, (CAR_WIDTH, CAR_HEIGHT))
        self.position = 'left'
        self.rect = self.image.get_rect(center=(LEFT_LANE_X + CAR_WIDTH // 2, SCREEN_HEIGHT - 150))

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
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(enemy_image, (CAR_WIDTH, CAR_HEIGHT))
        self.rect = self.image.get_rect(center=(random.choice([LEFT_LANE_X, RIGHT_LANE_X]) + CAR_WIDTH // 2, -CAR_HEIGHT))
        self.speed = speed

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > SCREEN_HEIGHT:
            self.reset_position()  # Reset posisi enemy jika keluar layar
            return True
        return False

    def reset_position(self):
        global last_lane
        # Pilih posisi yang berbeda dari kemunculan terakhir
        new_lane = random.choice([LEFT_LANE_X, RIGHT_LANE_X])
        while new_lane == last_lane:
            new_lane = random.choice([LEFT_LANE_X, RIGHT_LANE_X])
        self.rect.center = (new_lane + CAR_WIDTH // 2, -CAR_HEIGHT)
        last_lane = new_lane

    def draw(self):
        screen.blit(self.image, self.rect)

# Fungsi utama game
async def main():
    global game_over, score, speed, lane_marker_move_y  # Membuat variabel ini dapat diakses di seluruh fungsi
    player = Player()
    enemy = Enemy()
    score_display = pygwidgets.DisplayText(screen, (SCREEN_WIDTH // 2 - 50, 40), f"Score: {score}", fontSize=30, textColor=BLACK)
    title_display = pygwidgets.DisplayText(screen, (SCREEN_WIDTH // 2 - 70, 5), "Car Game", fontSize=40, textColor=BLACK)

    # Loop utama game
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

        if not game_over:
            screen.fill(GREY)  # Warna rumput di sekitar jalan
            
            # Warna abu-abu untuk kedua jalur
            pygame.draw.rect(screen, GREY, (LEFT_LANE_X - 70, 0, 300, SCREEN_HEIGHT))
            pygame.draw.rect(screen, YELLOW, (LEFT_LANE_X - 75, 0, 5, SCREEN_HEIGHT))  # Garis tepi kiri
            pygame.draw.rect(screen, YELLOW, (RIGHT_LANE_X + CAR_WIDTH + 70, 0, 5, SCREEN_HEIGHT))  # Garis tepi kanan
            
            # Garis putus-putus di tengah
            lane_marker_move_y += speed
            if lane_marker_move_y >= 60:
                lane_marker_move_y = 0
            for y in range(-60, SCREEN_HEIGHT, 60):
                pygame.draw.rect(screen, WHITE, (SCREEN_WIDTH // 2 - 5, y + lane_marker_move_y, 10, 40))

            player.draw()
            enemy.draw()
            if enemy.update():
                score += 10
                # Tingkatkan kecepatan setiap kelipatan skor tertentu
                if score % 50 == 0:
                    speed += 1
                    enemy.speed = speed

            # Cek tabrakan
            if pygame.sprite.collide_rect(player, enemy):
                collision_sound.play()
                screen.blit(crash_image, player.rect.topleft)
                pygame.display.flip()
                pygame.time.wait(1000)
                game_over = True
                score_display.setValue(f"Score: {score}")

            # Tampilan score
            score_display.setValue(f"Score: {score}")
            score_display.draw()
            title_display.draw()

        # Tampilkan pesan Game Over
        if game_over:
            game_over_display = pygwidgets.DisplayText(screen, (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2), "Game Over!", fontSize=50, textColor=BLACK)
            game_over_display.draw()
            pygame.display.flip()
            pygame.time.wait(2000)
            pygame.quit()
            sys.exit()

        pygame.display.update()
        await asyncio.sleep(0)
        clock.tick(FPS)

# Jalankan game
asyncio.run(main())
