import pygame

def process():
    events = pygame.event.get()

    for e in events:
        if e.type==pygame.QUIT:
            exit()