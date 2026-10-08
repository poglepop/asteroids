import pygame
import sys

from logger import log_state, log_event
from player import Player
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
	print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")

	# this is the initialization of the screen
	pygame.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	
	#Setting up the FFS
	clock = pygame.time.Clock()
	dt = 0.0
	

	#groups
	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	shots = pygame.sprite.Group()

	Player.containers = (updatable, drawable)
	Asteroid.containers = (updatable, drawable, asteroids)
	AsteroidField.containers = (updatable)
	Shot.containers = (shots, drawable, updatable)


	# instantiate player
	player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
	asteroid_field = AsteroidField()
	

	# this is the game loop
	while True:
		log_state()
		
		for event in pygame.event.get():
			if event.type ==pygame.QUIT:
				return
		dt=clock.tick(60)/1000
		#print(dt)

		screen.fill("black")

		for sprite in drawable:
			sprite.draw(screen)

		updatable.update(dt)
		
		for asteroid in asteroids:
			if player.collision(asteroid):
				log_event("player_hit")
				print("Game Over!")
				sys.exit()
				return
		
		for asteroid in asteroids:
			for shot in shots:
				if shot.collision(asteroid):
					log_event("asteroid_shot")
					asteroid.split()
					shot.kill()



		pygame.display.flip()
		

if __name__ == "__main__":
    main()
