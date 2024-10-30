import pygame, sys, random, asyncio
from pygame.math import Vector2

# Definisi Warna & OFFSET
WHITE = (130, 100, 130)
RED = (150, 40, 60)
BLACK = (0, 0, 0)
OFFSET = 50
# Definisi cell size & number
cell_size = 28  # ukuran gambar /perbesar / perkecil
cell_number = 20  # jumlah cell x=y

# Inisialisasi pygame dan font
pygame.init()
screen = pygame.display.set_mode((100 + cell_number * cell_size, 100 + cell_number * cell_size))
pygame.display.set_caption("Snake Pygame")
food = pygame.image.load("Asset/image/apple.png").convert_alpha()  # Path gambar

font_score = pygame.font.SysFont('Courier', 40)
font_title = pygame.font.SysFont('Courier', 30)

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 100)


# Kelas FOOD
class FOOD:
    def __init__(self):
        self.pos = self.generate_random_pos()

    def draw(self):
        food_rect = pygame.Rect(OFFSET + self.pos.x * cell_size, OFFSET + self.pos.y * cell_size, cell_size, cell_size)
        screen.blit(food, food_rect)

    def recreate(self, snake_body):
        self.pos = self.generate_random_pos()
        while self.pos in snake_body:
            self.pos = self.generate_random_pos()

    def generate_random_pos(self):
        x = random.randint(0, cell_number - 1)
        y = random.randint(0, cell_number - 1)
        pos = Vector2(x, y)
        return pos


# Kelas SNAKE
class SNAKE:
    def __init__(self):
        self.body = [Vector2(6, 9), Vector2(5, 9)]
        self.direction = Vector2(0, 1)
        self.add_segment = False

    def draw(self):
        for segment in self.body:
            pygame.draw.rect(screen, RED, (OFFSET + segment.x * cell_size, OFFSET + segment.y * cell_size, cell_size,
                                           cell_size), 0, 7)

    def update(self):
        if self.add_segment:
            self.body.insert(0, self.body[0] + self.direction)
            self.add_segment = False
        else:
            self.body = self.body[:-1]
            self.body.insert(0, self.body[0] + self.direction)

    def reset(self):
        self.body = [Vector2(6, 9), Vector2(5, 9), Vector2(4, 9)]
        self.direction = Vector2(1, 0)


# Kelas GAME
class GAME:
    def __init__(self):
        self.snake = SNAKE()
        self.food = FOOD()
        self.state = "STOPPED"
        self.score = 0

    def draw(self):
        self.snake.draw()
        self.food.draw()

    def update(self):
        if self.state != "STOPPED":
            self.snake.update()
            self.check_collision_with_food()
            self.check_collision_with_self()
            self.check_collision_with_edges()

    def check_collision_with_edges(self):
        if self.snake.body[0].x == cell_number or self.snake.body[0].x == -1:
            self.game_over()
        if self.snake.body[0].y == cell_number or self.snake.body[0].y == -1:
            self.game_over()

    def check_collision_with_self(self):
        headless_body = self.snake.body[1:]
        if self.snake.body[0] in headless_body:
            self.game_over()

    def check_collision_with_food(self):
        if self.food.pos == self.snake.body[0]:
            self.food.recreate(self.snake.body)
            self.snake.add_segment = True
            self.score += 1

    def game_over(self):
        self.snake.reset()
        self.food.recreate(self.snake.body)
        self.state = "STOPPED"
        self.score = 0


# Inisialisasi game
game = GAME()


# Fungsi utama dengan asyncio
async def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and game.snake.direction.y != 1:
                    game.snake.direction = Vector2(0, -1)
                if event.key == pygame.K_DOWN and game.snake.direction.y != -1:
                    game.snake.direction = Vector2(0, 1)
                if event.key == pygame.K_LEFT and game.snake.direction.x != 1:
                    game.snake.direction = Vector2(-1, 0)
                if event.key == pygame.K_RIGHT and game.snake.direction.x != -1:
                    game.snake.direction = Vector2(1, 0)
                if game.state == "STOPPED":
                    game.state = "RUNNING"

            if event.type == SCREEN_UPDATE:
                game.update()

        # Menggambar latar belakang
        screen.fill(WHITE)

        # Tampilkan skor dan judul
        score_text = font_score.render("SCORE ANDA : " + str(game.score), True, BLACK)
        title_text = font_title.render("SNAKE - PYGAME & PYGWIDGET", True, BLACK)
        screen.blit(score_text, (40, cell_number * cell_size + OFFSET + 10))
        screen.blit(title_text, (40, 10))

        # Buat dinding pembatas
        pygame.draw.rect(screen, BLACK, (45, 45, cell_size * cell_number + 10, cell_size * cell_number + 10), 5)

        # Menggambar objek game
        game.draw()
        pygame.display.update()

        # Tambahkan await asyncio.sleep(0) di akhir loop
        await asyncio.sleep(0)


# Jalankan loop asyncio utama
asyncio.run(main())
