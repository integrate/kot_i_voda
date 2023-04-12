import pygame, model

def process():
    events = pygame.event.get()

    for e in events:
        if e.type==pygame.QUIT:
            exit()

        if e.type==pygame.KEYDOWN and e.key==pygame.K_TAB:
            model.show_rects = not model.show_rects