# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
#from pygame.locals import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from circleshape import CircleShape
import sys
from bullet import Shot

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    #player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, drawable, updatable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots,updatable,drawable)
    asteroid_field = AsteroidField()
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")     
        for dra in drawable:
            dra.draw(screen)
        for upd in updatable:
            upd.update(dt)
        for ast in asteroids:
            if player.collision(ast):
                print("Game Over!")
                sys.exit(0)
            for bull in shots: 
                if bull.collision(ast):
                    ast.split()
                    bull.kill()
            
        pygame.display.flip()
        dt = clock.tick(60) / 1000
        #print(dt)
        
    
    
    #print(pygame.get_init())








if __name__ == "__main__":
    main()
