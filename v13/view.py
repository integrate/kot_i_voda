import pygame

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

water = pygame.image.load("../pics/water.png")
water = pygame.transform.scale(water, model.water_rect.size)

def draw():

    screen.fill([0, 0, 0])

    if model.side=="left":
        screen.blit(tom_left, model.tom_rect)
        screen.blit(umb_left, model.umb_rect)
        screen.blit(bucket_left, model.bucket_rect)
    else:
        screen.blit(tom_right, model.tom_rect)
        screen.blit(umb_right, model.umb_rect)
        screen.blit(bucket_right, model.bucket_rect)

    screen.blit(water, model.water_rect)
    pygame.draw.rect(screen, [52, 144, 193], model.under_water_rect)

    if model.show_rects:
        pygame.draw.rect(screen, [50, 100, 250], model.bucket_rect, 2)
        pygame.draw.rect(screen, [100, 200, 50], model.tom_rect, 2)
        pygame.draw.rect(screen, [200, 100, 50], model.umb_rect, 2)
        pygame.draw.rect(screen, [130, 70, 50], model.water_rect, 2)
        pygame.draw.rect(screen, [230, 170, 50], model.under_water_rect, 2)

    pygame.display.flip()