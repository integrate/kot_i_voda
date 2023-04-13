import pygame

def move_subjects_left():
    umb_rect.bottom=tom_rect.top+20
    umb_rect.right=tom_rect.right+20

    bucket_rect.bottom=tom_rect.top+35
    bucket_rect.left=tom_rect.left-18

def move_subjects_right():
    umb_rect.bottom=tom_rect.top+20
    umb_rect.left=tom_rect.left-20

    bucket_rect.bottom=tom_rect.top+35
    bucket_rect.right=tom_rect.right+18

def move_left():
    global side
    if side=="right":
        tom_rect.left+=140
    side = "left"
    tom_rect.left-=10
    if tom_rect.left<18:
        tom_rect.left = 18
    move_subjects_left()

def move_right():
    global side
    if side=="left":
        tom_rect.left-=140
    side = "right"
    tom_rect.left+=10
    if tom_rect.right>782:
        tom_rect.right = 782
    move_subjects_right()

screen = pygame.display.get_surface()

show_rects=True

tom_rect = pygame.rect.Rect(600, 200, 167, 126)
tom_rect.bottom = screen.get_height()

umb_rect = pygame.rect.Rect(100, 200, 100, 100)
bucket_rect = pygame.rect.Rect(100, 200, 60, 60)

cloud_rect = pygame.rect.Rect(100, 30, 90, 60)

side = "right"

move_subjects_right()