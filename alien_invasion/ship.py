import pygame
class Ship():

	def __init__(self,ai_settings, screen):
		"""initalized the ship position and the setting"""
		self.screen = screen
		self.ai_settings = ai_settings

		#loading the ship image
		self.image = pygame.image.load('images/ship3.png')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()

		#put the ship in the centre of the bottom
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom

		#save the min center value
		self.center = float(self.rect.centerx)

		#moving flag
		self.moving_right =False
		self.moving_left = False

	def update(self):
		"""moving position by given flag"""
		#updating the center value, not rect
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.center += self.ai_settings.ship_speed_factor

		if self.moving_left and self.rect.left:
			self.center -= self.ai_settings.ship_speed_factor

		#update the self.center and rect object
		self.rect.centerx = self.center

	def blitme(self):
		"""drawing the ship in giving position"""
		self.screen.blit(self.image, self.rect)