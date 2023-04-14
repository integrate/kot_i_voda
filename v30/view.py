import pygame

pygame.init()

screen = pygame.display.set_mode([800, 600])
import model

tom_left = pygame.image.load("../pics/cat1.png")
tom_right = pygame.transform.flip(tom_left, True, False)

umb_left = pygame.image.load("../pics/umbrella.png")
umb_left = pygame.transform.scale(umb_left, model.umb_rect.size)
umb_right = pygame.transform.flip(umb_left, True, False)

bucket_left = pygame.image.load("../pics/bucket.png")
bucket_left = pygame.transform.scale(bucket_left, model.bucket_rect.size)
bucket_right = pygame.transform.flip(bucket_left, True, False)

cloud = pygame.image.load("../pics/cloud.png")
cloud = pygame.transform.scale(cloud, model.cloud_rect.size)

sun = pygame.image.load("../pics/sun.png")
sun = pygame.transform.scale(sun, model.sun_rect.size)
sun = pygame.transform.flip(sun, True, False)

drop = pygame.image.load("../pics/water_drop.png")
drop = pygame.transform.scale(drop, model.drop_rect.size)

water = pygame.image.load("../pics/water.png")
water = pygame.transform.scale(water, model.water_rect.size)

raft = pygame.image.load("../pics/raft.png")
raft = pygame.transform.scale(raft, model.raft_rect.size)

f = pygame.font.SysFont("arial", 25, True)


def drop_text_str(drop_count):
    if drop_count >= 11 and drop_count <= 14:
        return "капель"

    last_digit = drop_count % 10
    if last_digit == 1:
        return "капля"
    if last_digit >= 2 and last_digit <= 4:
        return "капли"

    return "капель"


def draw():
    screen.fill([0, 0, 0])

    screen.blit(water, model.water_rect)
    pygame.draw.rect(screen, [52, 144, 193], model.under_water_rect)
    screen.blit(raft, model.raft_rect)

    if model.side == "left":
        screen.blit(tom_left, model.tom_rect)
        screen.blit(umb_left, model.umb_rect)
        screen.blit(bucket_left, model.bucket_rect)
    else:
        screen.blit(tom_right, model.tom_rect)
        screen.blit(umb_right, model.umb_rect)
        screen.blit(bucket_right, model.bucket_rect)

    drops_text = f.render(str(model.drop_count) + " " + drop_text_str(model.drop_count), True, [8, 48, 255])
    screen.blit(drops_text, [20, 10])

    drops_left = f.render(str(model.drops_left) + " " + drop_text_str(model.drops_left)+" до ускорения", True, [8, 48, 255])
    screen.blit(drops_left, [20, 40])

    level = f.render(str(model.level) + " уровень", True, [8, 48, 255])
    screen.blit(level, [20, 70])

    if model.show_sun:
        screen.blit(sun, model.sun_rect)
    screen.blit(cloud, model.cloud_rect)

    if model.drop_rect_visible:
        screen.blit(drop, model.drop_rect)

    if model.show_rects:
        pygame.draw.rect(screen, [50, 100, 250], model.bucket_rect, 2)
        pygame.draw.rect(screen, [100, 200, 50], model.tom_rect, 2)
        pygame.draw.rect(screen, [200, 100, 50], model.umb_rect, 2)

        pygame.draw.rect(screen, [50, 250, 250], model.cloud_rect, 2)
        t = f.render(str(model.cloud_speed), True, [50, 250, 250])
        screen.blit(t, model.cloud_rect)

        pygame.draw.rect(screen, [255, 142, 24], model.sun_rect, 2)

        if model.drop_rect_visible:
            pygame.draw.rect(screen, [50, 20, 250], model.drop_rect, 2)

        pygame.draw.rect(screen, [130, 70, 50], model.water_rect, 2)
        t = f.render(str(model.water_size), True, [50, 250, 250])
        screen.blit(t, model.water_rect)

        pygame.draw.rect(screen, [230, 170, 50], model.under_water_rect, 2)
        pygame.draw.rect(screen, [230, 170, 250], model.raft_rect, 2)

    pygame.display.flip()
