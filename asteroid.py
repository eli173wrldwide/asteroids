import pygame, random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)



    
    def draw(self, screen):
        # sub-classes must override
        pygame.draw.circle(screen, 
                           (255,255,255),
                           (self.position.x, self.position.y), 
                           self.radius,
                           2)
    def update(self, dt):
       self.position += dt * self.velocity   # sub-classes must override
 
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        random_angle = random.uniform(20, 50)
        velocity1 = self.velocity.rotate(random_angle)
        velocity2 = self.velocity.rotate(-random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        new_aster_1 = Asteroid(self.position.x, self.position.y, new_radius)
        new_aster_1.velocity = velocity1 * 1.2
    
        new_aster_2 = Asteroid(self.position.x, self.position.y, new_radius)
        new_aster_2.velocity = velocity2 * 1.2         
