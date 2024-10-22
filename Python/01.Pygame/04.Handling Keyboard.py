import pygame

#inisialisasi pygame
pygame.init()

#ukuran window
screen_width = 800
screen_height = 600

#membuat windows
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
        elif event.type == pygame.KEYDOWN:
            #mendeteksi tombol keyboard ditekan
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_UP:
                print("Up arrow key pressed")
            elif event.key == pygame.K_DOWN:
                print("Down arrow key pressed")

#keluar dari pygame
pygame.quit()