import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen,"white",self.position, self.radius, 2)

    def update(self, dt):
        self.position += dt * self.velocity

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        angle = random.uniform(20, 50)
        vect1 = pygame.math.Vector2.rotate(self.velocity, angle)
        vect2 = pygame.math.Vector2.rotate(self.velocity, -angle)
        new_rad = self.radius - ASTEROID_MIN_RADIUS
        NewAst1 = Asteroid(self.position.x, self.position.y, new_rad)
        NewAst1.velocity = vect1 * 1.2
        NewAst2 = Asteroid(self.position.x, self.position.y, new_rad)
        NewAst2.velocity = vect2 * 1.2