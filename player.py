from circleshape import CircleShape
from shot import Shot
import constants as ct 
import pygame


class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, ct.PLAYER_RADIUS)
        self.rotation = 0
        self.shoot_timer = 0.0

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]    

    def rotate(self, dt):
        self.rotation += ct.PLAYER_TURN_SPEED * dt

    def draw(self, screen):
        pygame.draw.polygon(screen, (255, 255, 255), self.triangle(), 2)

    def shoot(self):
        if(self.shoot_timer > 0):
            return
        shot = Shot(self.position.x, self.position.y)
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * ct.PLAYER_SHOOT_SPEED
        self.shoot_timer = ct.PLAYER_SHOOT_COOLDOWN


    def update(self, dt):
        self.shoot_timer -= dt
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)    
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            forward = pygame.Vector2(0, 1).rotate(self.rotation)
            self.position += forward * ct.PLAYER_SPEED * dt
        if keys[pygame.K_s]:
            back = pygame.Vector2(0, 1).rotate(self.rotation)
            self.position += back * ct.PLAYER_SPEED * (-dt)

        if keys[pygame.K_SPACE]:
            self.shoot()

