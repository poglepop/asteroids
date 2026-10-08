import pygame
import random

from circleshape import  CircleShape
from constants import PLAYER_RADIUS, LINE_WIDTH, PLAYER_TURN_SPEED, PLAYER_SPEED, ASTEROID_MIN_RADIUS, ASTEROID_KINDS, ASTEROID_SPAWN_RATE_SECONDS, ASTEROID_MAX_RADIUS

from logger import log_state, log_event

class Asteroid(CircleShape):
    def __init__(self,x: int, y: int, radius: int) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update (self, dt: float) -> None:
        self.position += self.velocity * dt
    
    def split(self) -> list["Asteroid"]:
        self.kill()

        if self.radius <= 20:
            return []
        else:
            log_event("asteroid_split")
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
            random_angle = random.randint(20, 50)
            asteroid1.velocity = self.velocity.rotate(random_angle) *  1.2
            asteroid2.velocity = self.velocity.rotate(-random_angle) *  1.2
            
            return [asteroid1, asteroid2]
