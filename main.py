import pygame
import constants as ct



def main():
    print("Starting Astroids!")
    print("Screen width:", ct.SCREEN_WIDTH)
    print("Screen height:", ct.SCREEN_HEIGHT)
    pygame.init()
    screen = pygame.display.set_mode((ct.SCREEN_WIDTH, ct.SCREEN_HEIGHT))
    while(True):
        for event in pygame.event.get(): # this makes close button to work
            if event.type == pygame.QUIT:
                return
        screen.fill((0, 0, 0))
        pygame.display.flip()


if __name__ == "__main__":
    main()
