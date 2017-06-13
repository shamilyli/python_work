import sys
import pygame

from settings import Settings
from ship import Ship
from alien import Alien
from pygame.sprite import Group



import game_functions as gf

def run_game():
	#inisitalized the game and create a screen object
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption("Alien Ivasion")

	#create a ship
	ship = Ship(ai_settings,screen)
	#create a alien
	alien = Alien(ai_settings, screen)
	#creating a group to save bullets
	bullets = Group()
	aliens= Group()

	gf.create_fleet(ai_settings,screen,ship,aliens)

	#start the game in the loop
	while True:
		
		#event keyboard and mouse
		gf.check_events(ai_settings,screen,ship,bullets)
		ship.update()
		gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
		gf.update_aliens(ai_settings,aliens)
		gf.update_screen(ai_settings,screen,ship,aliens,bullets)

run_game()