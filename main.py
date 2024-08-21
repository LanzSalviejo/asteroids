import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()
    
    Player.containers = (updatable, drawable)
    
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    dt = 0
    
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        #player.update(dt)
        for obj in updatable:
            obj.update(dt)
            
        for asteroid in asteroids:
            if player.collision(asteroid):
                print("Game Over!")
                sys.exit()
            for shot in shots:
                if shot.collision(asteroid):
                    shot.kill()
                    asteroid.split()
                    
        screen.fill("black")
        
        for obj in drawable:
            obj.draw(screen)
                    
        #player.draw(screen)
        pygame.display.flip()
        
        # limit framerate
        dt = clock.tick(144) / 1000
        
if __name__ == "__main__":
    main()