import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode(size=(SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    group_updatable = pygame.sprite.Group()
    group_drawable = pygame.sprite.Group()
    group_asteroids = pygame.sprite.Group()
    group_shots = pygame.sprite.Group()

    Player.containers = (group_updatable, group_drawable)
    Asteroid.containers = (group_updatable, group_drawable, group_asteroids)
    AsteroidField.containers = (group_updatable)
    Shot.containers = (group_drawable, group_updatable, group_shots)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    dt = 0

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        group_updatable.update(dt)
            
        for asteroid in group_asteroids:
            if asteroid.collision_detect(player):
                print("Game Over!")
                return

            for bullet in group_shots:
                if bullet.collision_detect(asteroid):
                    bullet.kill()
                    asteroid.split_asteroid()
            
            
        screen.fill("black")

        for member in group_drawable:
            member.draw(screen)

        pygame.display.flip()

        # limits to 60 fps
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
