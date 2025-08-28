import pygame
from player import Player
from asteroid import Asteroid
from shot import Shot
from asteroidfield import AsteroidField
import constants as ct



def main():
    print("Starting Astroids!")
    print("Screen width:", ct.SCREEN_WIDTH)
    print("Screen height:", ct.SCREEN_HEIGHT)
    pygame.init()

    screen = pygame.display.set_mode((ct.SCREEN_WIDTH, ct.SCREEN_HEIGHT))

    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Shot.containers = (shots, updatable, drawable)

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()

    Player.containers = (updatable, drawable)
    player = Player(ct.SCREEN_WIDTH/2, ct.SCREEN_HEIGHT/ 2)

    dt = 0

    while(True):
        for event in pygame.event.get(): # this makes close button to work
            if event.type == pygame.QUIT:
                return
        updatable.update(dt)

        for item in asteroids:
            if player.collison(item):
                print("Game Over")
                return
            for bullet in shots:
                if bullet.collison(item):
                    bullet.kill()
                    item.split()

        screen.fill((0, 0, 0))
        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000 # second


if __name__ == "__main__":
    main()
