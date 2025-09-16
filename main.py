import pygame as pg
import time
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from ondeath import *

def main():
    pg.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")

    screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pg.time.Clock()
    dt = 0

    # Used to calculate score
    time_started = int(time.time())
    asteroids_hit = 0
 
    updatable = pg.sprite.Group()
    drawable = pg.sprite.Group()
    asteroids = pg.sprite.Group()
    shots = pg.sprite.Group()

    AsteroidField.containers = (updatable)
    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable, drawable)
    Shot.containers = (shots, updatable, drawable)

    player = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))
    asteroid_field = AsteroidField()

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
            
        screen.fill("black")
        updatable.update(dt)

        for asteroid in asteroids:
            if player.check_collide(asteroid): # Player dies
                on_death(time_started, asteroids_hit)

            for bullet in shots:
                if bullet.check_collide(asteroid): # Bullet hits asteroid
                    asteroids_hit += 1
                    bullet.kill()
                    asteroid.split()

        for object in drawable: 
            object.draw(screen)

        pg.display.flip()
        clock.tick(60)
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
