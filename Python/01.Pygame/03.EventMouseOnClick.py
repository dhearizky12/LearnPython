import pygame

#inisialisasi pygame
pygame.init()

#UKURAN WINDOW
screen_width = 800
screen_height = 600

#membuat window
screen = pygame.display.set_mode((screen_width, screen_height))

#warna latar belakang window
black = (0,0,0)

#mengeset latar belakang window menjadi warna hitam
screen.fill(black)

#menampilkan window
pygame.display.update()

#Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONUP:
            #mendeteksi klik mouse
            x,y= event.pos
            print("Mouse clicked at ", x, y)

#keluar dari Pygame
pygame.quit()