import pygame

# Inisialisasi Pygame
pygame.init()

# Ukuran window
screen_width = 800
screen_height = 600

#Membuat window
screen = pygame.display.set_mode((screen_width, screen_height))

player = pygame.Rect((300, 250, 50, 50))

#warna latar belakang window
black = (50,150,200)

#mengeset latar belakang window menjadi warna hitam
screen.fill(black)


#menampilkan window
pygame.display.update()

# game loop
running = True
while running:
    screen.fill((67,180,200))
    pygame.draw.rect(screen, (125,97,71), player)

    key = pygame.key.get_pressed()
    if key[pygame.K_a] == True:
        player.move_ip(-1,0)
    elif key[pygame.K_d] == True:
        player.move_ip(1,0)
    elif key[pygame.K_w] == True:
        player.move_ip(0,-1)
    elif key[pygame.K_s] == True:
        player.move_ip(0,2)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()

#Keluar dari pygame
pygame.quit()

