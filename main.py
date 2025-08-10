import pygame
from constants import *
from player import Player

def main():
    pygame.init()
    screen = pygame.display.set_mode(size=(SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    group_updatable = pygame.sprite.Group()
    group_drawable = pygame.sprite.Group()

    Player.containers = (group_updatable, group_drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    dt = 0

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill("black")

        for member in group_drawable:
            member.draw(screen)
        group_updatable.update(dt)

        pygame.display.flip()

        # limits to 60 fps
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
