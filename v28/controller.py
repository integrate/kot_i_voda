import pygame, random
import model

pygame.key.set_repeat(20)

cloud_timer = pygame.event.custom_type()
pygame.time.set_timer(cloud_timer, 3000)

drop_timer = pygame.event.custom_type()
pygame.time.set_timer(drop_timer, model.drop_time, 1)

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

        if e.type==model.sun_timer_id:
            model.hide_sun()

        if e.type == drop_timer:
            pygame.time.set_timer(drop_timer, model.drop_time, 1)
            model.make_drop()

        if e.type == pygame.KEYDOWN and e.key == pygame.K_RETURN:
            model.make_sun()

    model.show_rects = bool(pygame.key.get_pressed()[pygame.K_TAB])