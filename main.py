import pygame # type: ignore
import sys

from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot





def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    fps = 60
    
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    Shot.containers = (shots, updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()
    

    
    Player.containers = (updatable, drawable)
    player = Player(x, y)
    
    dt = 0
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        
        for action in updatable:
            action.update(dt)
        
        for asteroid in asteroids:
            if player.collision(asteroid):
                print("Game over!")
                sys.exit()
        
        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collision(shot):
                    asteroid.split()
                    shot.kill()
            
        screen.fill(("black"))
            
        for action in drawable:
            action.draw(screen)
            
        pygame.display.flip()
        
        dt = clock.tick(fps) / 1000
        
    
if __name__ == "__main__":
    main()