import pygame

#inisialisasi pygame
pygame.init()

#ukuran window
screen_width = 800
screen_height = 600

#membuat window
screen = pygame.display.set_mode((screen_width,screen_height))

#warna
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)


#game loop

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #menggambar garis
    pygame.draw.line(screen,red,(0,0), (800,600),5)

    #menggambar lingkaran
    pygame.draw.circle(screen,green,(400,300),50,0)

    #menggambar segitiga
    pygame.draw.polygon(screen,blue,[(100,100),(200,50),(300,100)],0)

    #menggambar elips
    pygame.draw.ellipse(screen, blue, (400, 200, 150,100),0)

    #update window
    pygame.display.update()

#keluar dari Pygame
pygame.quit()