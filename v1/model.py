import pygame

screen = pygame.display.get_surface()

tom_rect = pygame.rect.Rect(100, 200, 167, 126)
tom_rect.bottom = screen.get_height()