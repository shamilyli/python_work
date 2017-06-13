import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
	"""a class for shooting bullet"""

	def __init__(self, ai_settings, screen, ship):
		super(Bullet,self).__init__()
		self.screen = screen


		#creating rect bullet in (0,0) and set it in correct position
		self.rect = pygame.Rect(0,0, ai_settings.bullet_width, ai_settings.bullet_height)
		self.rect.centerx = ship.rect.centerx
		self.rect.top = ship.rect.top

		#saving the decimal number of bullet location
		self.y = float(self.rect.y)
		self.color = ai_settings.bullet_color
		self.speed_factor = ai_settings.bullet_speed_factor



	def update(self):
		"""moving the bullet"""
		#update the bullet position
		self.y -= self.speed_factor

		#update the rect position for bullet
		self.rect.y = self.y


	def draw_bullet(self):
		"""draw the bullet on the screen"""
		pygame.draw.rect(self.screen, self.color, self.rect)
