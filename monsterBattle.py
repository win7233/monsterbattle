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
		target.health -= self.attackPower # deal attackPower damage to Target
	def draw(self):
		monster_health_text = font.render(f'{self.name} = health:{self.health} ', True, self.colour) # render health text
		screen.blit(monster_health_text, (self.x-80,self.y-70))                                      # <- blit the health text to the screen
		pygame.draw.rect(self.screen, self.colour, (self.x,self.y,self.size,self.size))              # draw the actual monster
	

class Warrior(Monster):
	def __init__(self, hp, colour):
		super().__init__(hp, colour)
		self.name = "Warrior" # rename monster
		self.attackPower = 7 # raise attackpower from base
	def attack(self, target):
		"""
		deal a random amount of damage between 2 and attackpower (7)
		"""
		target.health -= random.randint(2,self.attackPower)

class Mage(Monster):
	def __init__(self, hp, colour):
		super().__init__(hp, colour)
		self.name = "Mage"
		self.attackPower = 10 # raise attackpower quite a bit from base
	def attack(self, target):
		"""
		deals either 10 or 0 damage (50/50)
		"""
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
		self.kills = 0 # unique to player: number of monsters you've killed
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
		"""
		deals a random number between minattackpower (4) and maxattackpower(9)
		"""
		attackDamageTotal = random.randint(self.minAttackPower,self.maxAttackPower) # calculate attackDamageTotal
		target.health -= attackDamageTotal # deal attackDamageTotal damage to target
		self.attackText = font.render(f'{self.name} attacks {target.name} with {attackDamageTotal}', True, RED) # render attackText object
		screen.blit(self.attackText, (400, 200)) # blit attackText object to screen above character


# == functions??? ==
def recycle():
	"""
	generate a new monster
	"""
	return random.choice([Warrior(30,ORANGE),Mage(30,BLUE), Troll(30,YELLOW)])

# == GAME RUN VARS ==
running = True
playerObject = Player()
currentEnemy = recycle()
# == GAME LOOP ==
screen.fill(WHITE)
start_text = font.render(f'PRESS [SPACE] TO START', True, RED)
screen.blit(start_text, (600, 300))

while running:
	# event handling
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False # kill program
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_SPACE:
				## == MAIN GAME LOOP == 
				if playerObject.health >= 0: # if player is alive
					# = player handling
					playerObject.attack(currentEnemy) # player attack enemy
					screen.fill(WHITE) # clear screen
					playerObject.draw() # draw player
					playerObject.attack(currentEnemy)
					# = enemy handling
					if currentEnemy.health <= 0: # replace dead enemies
						currentEnemy = recycle()
						playerObject.kills += 1
					elif currentEnemy.health >= 0: # if enemy is alive attack
						currentEnemy.attack(playerObject)
					currentEnemy.draw()
				elif playerObject.kills >= 3: # if winstate
					## == WIN SCREEN ==
					screen.fill(WHITE) # clear screen (to remove previous game frames)
					win_text = font.render(f'YOU WIN!', True, RED)
					screen.blit(win_text, (640, 300))
				else:
					## == loss SCREEN == (hehe loss)
					screen.fill(WHITE) # clear screen (to remove previous game frames)
					loss_text = font.render(f'YOU LOSE! (good day) -ref', True, RED)
					screen.blit(loss_text, (640, 300))
	pygame.display.flip()
	clock.tick(FPS)