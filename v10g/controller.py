import pygame, random
import model

pygame.key.set_repeat(20)

cloud_timer = pygame.event.custom_type()
pygame.time.set_timer(cloud_timer, 3000)

def process():
    events = pygame.event.get()

    for e in events:
        if e.type==pygame.QUIT:
            exit()

        if e.type == pygame.KEYDOWN and e.key == pygame.K_LEFT:
            model.move_left()
        if e.type == pygame.KEYDOWN and e.key == pygame.K_RIGHT:
            model.move_right()

        if e.type == cloud_timer:
            model.cloud_change()

    model.show_rects = bool(pygame.key.get_pressed()[pygame.K_TAB])