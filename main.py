import pygame as pg
from constants import *
from player import Player

def main():
    pg.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")

    screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pg.time.Clock()
    dt = 0

    player = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
            
        screen.fill("black")
        player.draw(screen)

        pg.display.flip()
        clock.tick(60)
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
