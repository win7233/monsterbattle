# monster battle game
# win7233

import pygame
import random
import math 

# == CONSTANTS == 
SCREENWIDTH = 1280
SCREENHEIGHT = 800

screen = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
pygame.display.set_caption('Monster Battle game yay!')
font = pygame.font.Font(None,36)

FPS = 60

# == COLOURS ==
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
YELLOW = (255,255,0)
ORANGE = (255,165,0)

# == CLASSES ==

class Monster:
	"""
	base class for monsters
	"""
	def __init__(self, hp, colour):
		self.name = "monster"
		self.health = hp
		self.colour = colour
		self.attackPower = 5
		self.x = 800
		self.y = 400
		self.screen = screen
	def attack(self, target):
		target.health -= self.attackPower
	def draw(self):
		points = [
			(self.x, self.y - self.size)
			(self.x + self.size)
			(self.x, self.y + self.size)
			(self.x - self.size, self.y)
		]
		score_text = font.render(f'{self.name} = health:{self.health} ', True, self.colour)
		screen.blit(score_text, (self.x,self.y-50))

		pygame.draw.polygon(self.screen, self.colour, points)
	

class Warrior(Monster):
	def __init__(self, hp, colour):
		super().__init__(hp, colour)
		self.name = "Warrior"
		self.attackPower = 7
	def attack(self, target):
		target.health -= random.randint(2,self.attackPower)

class Mage(Monster):
	def __init__(self, name, hp, colour):
		super().__init__(hp, colour)
		self.name = "Mage"
		self.attackPower = 10
	def attack(self, target):
		if random.randint(0,1):
			target.health -= self.attackPower

class Troll(Monster):
	def __init__(self, name, hp, colour):
		super().__init__(hp, colour)
		self.name = "Troll"
		self.attackPower = 3
	def attack(self, target):
		target.health -= self.attackPower
		self.health += 2
