import pygame

screen = pygame.display.set_mode([800, 600])
import model

tom = pygame.image.load("../pics/cat1.png")


def draw():

    screen.fill([0, 0, 0])

    screen.blit(tom, model.tom_rect)
    pygame.draw.rect(screen, [100, 200, 50], model.tom_rect, 2)

    pygame.display.flip()