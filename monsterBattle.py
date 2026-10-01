# monster battle game
# win7233

import pygame
import random
import math 
pygame.init()
# == CONSTANTS == 
SCREENWIDTH = 1280
SCREENHEIGHT = 800

screen = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
pygame.display.set_caption('Monster Battle game yay!')
font = pygame.font.Font(None,36)

clock = pygame.time.Clock()

FPS = 60

# == COLOURS ==
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
YELLOW = (200,200,80)
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
		self.size = 30
		self.screen = screen
	def attack(self, target):
		target.health -= self.attackPower
	def draw(self):
		monster_health_text = font.render(f'{self.name} = health:{self.health} ', True, self.colour)
		screen.blit(monster_health_text, (self.x-80,self.y-70))
		pygame.draw.rect(self.screen, self.colour, (self.x,self.y,self.size,self.size))
	

class Warrior(Monster):
	def __init__(self, hp, colour):
		super().__init__(hp, colour)
		self.name = "Warrior"
		self.attackPower = 7
	def attack(self, target):
		target.health -= random.randint(2,self.attackPower)

class Mage(Monster):
	def __init__(self, hp, colour):
		super().__init__(hp, colour)
		self.name = "Mage"
		self.attackPower = 10
	def attack(self, target):
		if random.randint(0,1):
			target.health -= self.attackPower

class Troll(Monster):
	def __init__(self, hp, colour):
		super().__init__(hp, colour)
		self.name = "Troll"
		self.attackPower = 3
	def attack(self, target):
		target.health -= self.attackPower
		self.health += 2

class Player(Monster):
	def __init__(self):
		self.name = "player"
		self.health = 30
		self.colour = GREEN
		self.maxAttackPower = 9
		self.minAttackPower = 4
		self.x = 480
		self.y = 400
		self.size = 40
		self.screen = screen
	def attack(self, target):
		attackDamageTotal = random.randint(self.minAttackPower,self.maxAttackPower)
		target.health -= attackDamageTotal
		self.attackText = font.render(f'{self.name} attacks {target.name} with {attackDamageTotal}', True, RED)
		screen.blit(self.attackText, (400, 200))


# == functions??? ==
def recycle():
	return random.choice([Warrior(30,ORANGE),Mage(30,BLUE), Troll(30,YELLOW)])
# == GAME RUN VARS ==
running = True
playerObject = Player()
currentEnemy = recycle()
# == GAME LOOP ==
screen.fill(WHITE)
start_text = font.render(f'PRESS [SPACE] TO START', True, RED)
screen.blit(start_text, (640, 300))


while running:
	# event handling
	for event in pygame.event.get():
		if event.type == pygame.QUIT or playerObject.health <= 0:
			running = False
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_SPACE:
				playerObject.attack(currentEnemy)
				screen.fill(WHITE)
				playerObject.draw()
				playerObject.attack(currentEnemy)
				if currentEnemy.health <= 0:
					currentEnemy = recycle()
				else:	
					currentEnemy.attack(playerObject)
					currentEnemy.draw()
	pygame.display.flip()
	clock.tick(FPS)