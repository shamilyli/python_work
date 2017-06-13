import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
	"""class of alien"""

	def __init__(self, ai_settings,screen):
		"""initialized alien with position"""
		super(Alien, self).__init__()
		self.screen = screen
		self.ai_settings = ai_settings

		#loading alien image, and setting the rect
		self.image = pygame.image.load('images/alien3.png')
		self.rect = self.image.get_rect()

		#
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height

		self.x = float(self.rect.x)

	def blitme(self):
		self.screen.blit(self.image, self.rect)

	def update(self):
		"""moving the aliens to the right or left"""
		self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
		self.rect.x = self.x

	def check_edges(self):
		"""if the alien at the screen edge, then return True"""
		screen_rect = self.screen.get_rect()
		if self.rect.right >= screen_rect.right:
			return True
		elif self.rect.left <=0:
			return True

