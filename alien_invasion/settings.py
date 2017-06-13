class Settings():
	"""a class for all settings in the game"""

	def __init__(self):
		""" inital the game setting"""
		self.screen_width = 1200
		self.screen_height = 800
		self.bg_color = (230,230,230) #RGB 0 - 255

		self.ship_speed_factor = 1.5

		#setting for the bullet
		self.bullet_speed_factor =3
		self.bullet_width =300
		self.bullet_height =15
		self.bullet_color = 60,60,60
		self.bullets_allowed = 5

		#setting for the alien
		self.alien_speed_factor =1
		self.fleet_drop_speed =10

		#fleet_direction moving to the right
		self.fleet_direction =1