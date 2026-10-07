import pygame
from circleshape import  CircleShape
from constants import PLAYER_RADIUS, LINE_WIDTH, PLAYER_TURN_SPEED, PLAYER_SPEED

class Asteroid(CircleShape):
    def __init__(self,x: int, y: int, radius: int) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update (self, dt: float) -> None:
        self.position += self.velocity * dt
