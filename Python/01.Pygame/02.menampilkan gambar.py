import pygame

# inisialisasi pygame
pygame.init()

# ukuran window
screen_width = 800
screen_height = 600

# membuat window
screen = pygame.display.set_mode((screen_width, screen_height))

# membuat gambar
image = pygame.image.load("Python\\01.Pygame\\image.png")
# menggambar ulang gambar di tengah window
screen.blit(image, (screen_width // 2 - image.get_width() // 2,
                    screen_height // 2 - image.get_height() // 2))

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    

    # memperbarui layar
    pygame.display.update()

# keluar dari Pygame
pygame.quit()
