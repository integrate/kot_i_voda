import pygame, random

def move_subjects_left():
    umb_rect.bottom=tom_rect.top+20
    umb_rect.right=tom_rect.right+20

    bucket_rect.bottom=tom_rect.top+35
    bucket_rect.left=tom_rect.left-18

    raft_rect.left = tom_rect.left

def move_subjects_right():
    umb_rect.bottom=tom_rect.top+20
    umb_rect.left=tom_rect.left-20

    bucket_rect.bottom=tom_rect.top+35
    bucket_rect.right=tom_rect.right+18

    raft_rect.right = tom_rect.right

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


def cloud_change():
    global cloud_speed, drop_rect, drop_rect_visible
    r = random.randint(1, 2)
    if r == 1:
        cloud_speed = -cloud_speed

    drop_rect_visible = True
    drop_rect.top = cloud_rect.bottom
    drop_rect.centerx = cloud_rect.centerx


def go_go_go():
    global cloud_speed, water_size, drop_rect_visible
    cloud_rect.left+=cloud_speed
    if cloud_rect.left<0:
        cloud_speed =-cloud_speed
    if cloud_rect.right>screen.get_width():
        cloud_speed =-cloud_speed

    drop_rect.y+=3
    if drop_rect_visible:
        if drop_rect.colliderect(water_rect):
            water_size+=3
            drop_rect_visible=False
            make_water()
        elif drop_rect.colliderect(umb_rect):
            drop_rect_visible = False
        elif drop_rect.colliderect(bucket_rect):
            drop_rect_visible = False


def make_water():
    global under_water_rect, water_rect
    under_water_rect = pygame.rect.Rect(0, 0, screen.get_width(), water_size - 30)
    under_water_rect.bottom = screen.get_height()

    water_rect = pygame.rect.Rect(0, 0, screen.get_width(), 30)
    water_rect.bottom = under_water_rect.top

    raft_rect.bottom = water_rect.top + 30
    tom_rect.bottom = raft_rect.top+15

    if side=="right":
        move_subjects_right()
    else:
        move_subjects_left()

screen = pygame.display.get_surface()

show_rects=True

tom_rect = pygame.rect.Rect(600, 200, 167, 126)
tom_rect.bottom = screen.get_height()

umb_rect = pygame.rect.Rect(100, 200, 100, 100)
bucket_rect = pygame.rect.Rect(100, 200, 60, 60)

cloud_rect = pygame.rect.Rect(100, 30, 90, 60)
cloud_speed = 1

drop_rect = pygame.Rect(100, 200, 15, 22)
drop_rect_visible = False

water_size = 30

under_water_rect = pygame.rect.Rect(0, 0, screen.get_width(), water_size-30)
under_water_rect.bottom=screen.get_height()

water_rect = pygame.rect.Rect(0, 0, screen.get_width(), 30)
water_rect.bottom=under_water_rect.top

raft_rect=pygame.Rect(100, 0, 250, 30)
raft_rect.bottom=water_rect.top+30

side = "right"

move_subjects_right()