import pygame

#inisialisasi pygame
pygame.init()

#ukuran window
screen_width = 800
screen_height = 600

#membuat window
screen = pygame.display.set_mode((screen_width, screen_height))

#warna latar belakang
black = (0,0,0)

#mengeset latar belakang window menjadi warna hitam
screen.fill(black)

#warna persegi
red = (255,0,0)

#ukuran persegi
rect_width = 100
rect_height = 50

#posisi persegi
rect_x = (screen_width - rect_width) // 2
rect_y = (screen_height - rect_height) //2 

#membuat objek persegi
rect = pygame.Rect(rect_x, rect_y, rect_width, rect_height)

#menggambar persegi ke window
pygame.draw.rect(screen,red,rect)

#menampilkan window
pygame.display.update()

#Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

#keluar dari Pygame
pygame.quit()
