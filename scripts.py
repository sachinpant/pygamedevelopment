import pygame

black =(0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

pygame.init()

screenSize = (800,600)
screen = pygame.display.set_mode(screenSize)

pygame.display.set_caption("Clash of Clans")

clock = pygame.time.Clock()

loopExit = True
while loopExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loopExit = False

    screen.fill(green)

    clock.tick(20)

    pygame.display.flip()

pygame.quit()
