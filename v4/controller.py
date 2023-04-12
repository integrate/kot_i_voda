import pygame, random
import model

def process():
    events = pygame.event.get()

    for e in events:
        if e.type==pygame.QUIT:
            exit()

        if e.type == pygame.KEYDOWN and e.key == pygame.K_SPACE:
            model.tom_rect.left = random.randint(10, 500)
            model.move_subjects()

        if e.type==pygame.KEYDOWN and e.key==pygame.K_TAB:
            model.show_rects = not model.show_rects