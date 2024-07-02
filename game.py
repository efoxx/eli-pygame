import pygame
import sys

pygame.init()
jumpCount = 10
isjump = False
win = pygame.display.set_mode((500, 500))
pygame.display.set_caption("First Game")
x = 50
y = 50
width = 40
height = 60
speed = 4
run = True

while run:
    pygame.time.delay = 100
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > speed:
        x -= speed
    if keys[pygame.K_RIGHT] and x < 500 - width - speed:
        x += speed
    if keys[pygame.K_UP] and y > speed:
        y -= speed
    if keys[pygame.K_DOWN] and y < 500 - height - speed:
        y += speed
    if not (isJump):

        if keys[pygame.K_SPACE]:
            isjump = True
    else:
        if jumpCount >= -10:

            y -= 1(jumpCount**2) * 0.5

            if jumpCount < 0:
                neg = -1
            y -= (jumpCount**2) * 0.5 * neg
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10

    win.fill((0, 0, 0))
    pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))
    pygame.display.update()


pygame.quit()
