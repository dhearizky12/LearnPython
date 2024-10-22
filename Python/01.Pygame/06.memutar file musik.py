import pygame

#inisialisasi pygame
pygame.init()

#memuat file suara
sound = pygame.mixer.Sound("Python\\01.Pygame\\sound.wav")

#memutar suara
sound.play()

#Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

#keluar dari Pygame
pygame.quit()
