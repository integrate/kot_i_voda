import pygame

screen = pygame.display.get_surface()

tom_rect = pygame.rect.Rect(100, 200, 167, 126)
tom_rect.bottom = screen.get_height()

umb_rect = pygame.rect.Rect(100, 200, 100, 100)
umb_rect.bottom=tom_rect.top+20
umb_rect.right=tom_rect.right+20

bucket_rect = pygame.rect.Rect(100, 200, 60, 60)
bucket_rect.bottom=tom_rect.top+35
bucket_rect.left=tom_rect.left-18