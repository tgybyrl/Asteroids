import pygame
from logger import log_event
import random
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
  def __init__(self, x, y, radius):
    super().__init__(x, y, radius)


  def draw(self, screen):
    pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

  def update(self, dt):
    self.position += self.velocity * dt

  def split(self):
    pygame.sprite.Sprite.kill(self)
    if self.radius <= ASTEROID_MIN_RADIUS:
      return
    else:
      log_event("asteroid_split")
      random_angle = random.uniform(20, 50)
      rotated_velocity_with_angle = self.velocity.rotate(random_angle)
      opposite_rotated_velocity_with_angle = self.velocity.rotate(-random_angle)
      new_radius = self.radius - ASTEROID_MIN_RADIUS
      asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
      asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)
      asteroid_1.velocity = rotated_velocity_with_angle * 1.5
      asteroid_2.velocity = opposite_rotated_velocity_with_angle * 1.5