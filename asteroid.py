from circleshape import CircleShape
import constants as ct
import random as rand
import pygame

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius,2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ct.ASTEROID_MIN_RADIUS:
            return
        angle = rand.uniform(20, 50)
        v1 = self.velocity.rotate(angle)
        v2 = self.velocity.rotate(-angle)
        new_radius = self.radius - ct.ASTEROID_MIN_RADIUS
        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid1.velocity = v1 * ct.ASTEROID_SPLIT_SPEED_MULTIPLIER
        asteroid2.velocity = v2 * ct.ASTEROID_SPLIT_SPEED_MULTIPLIER

