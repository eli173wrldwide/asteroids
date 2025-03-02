from constants import *
import pygame, sys
from player import Player
from asteroidfield import AsteroidField
from asteroid import Asteroid
from shot import Shot

def main():
    
    pygame.init()
    
    shots = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,) 
    Shot.containers = (shots, updatable, drawable) 
    
    new_field = AsteroidField() 
    new_player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))   
    while True: 
        dt = clock.tick(60)/1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill((0,0,0))
        updatable.update(dt)
        
        for a in asteroids:
            if new_player.col_check(a):
                print("Game over!")
                sys.exit()

        for a in asteroids:
            for b in shots:
                if a.col_check(b):
                    a.split()
                    b.kill()

        for i in drawable:
            i.draw(screen)
        pygame.display.flip()


    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__": 
    main() 
