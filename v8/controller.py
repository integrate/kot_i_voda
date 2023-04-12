import pygame, random
import model

pygame.key.set_repeat(20)

def process():
    events = pygame.event.get()

    for e in events:
        if e.type==pygame.QUIT:
            exit()

        if e.type == pygame.KEYDOWN and e.key == pygame.K_LEFT:
            model.move_left()
        if e.type == pygame.KEYDOWN and e.key == pygame.K_RIGHT:
            model.move_right()