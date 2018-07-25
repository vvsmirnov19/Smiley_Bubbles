import pygame
import random
import time
black = (0, 0, 0)
pygame.init()
screen = pygame.display.set_mode([800, 600])
pic = pygame.image.load('CrazySmile.bmp')
colorkey = pic.get_at((0,0))
pic.set_colorkey(colorkey)
spritelist = pygame.sprite.Group()
clock = pygame.time.Clock()
going=True
mouse=False
class Smiley(pygame.sprite.Sprite):
	pos = (0,0)
	xvel = 1
	yvel = 1
	scale = 10
	def __init__(self, pos, xvel, yvel):
		pygame.sprite.Sprite.__init__(self)
		self.image = pic
		self.scale = 10
		self.image = pygame.transform.scale(self.image, (self.scale,self.scale))
		self.rect = self.image.get_rect()
		self.pos = pos
		self.rect.x = pos[0] - self.scale/2
		self.rect.y = pos[1] - self.scale/2
		self.xvel = xvel
		self.yvel = yvel
	def update(self):
		self.rect.x += self.xvel
		self.rect.y += self.yvel
		if self.rect.x <= 0 or self.rect.x > screen.get_width() - self.scale:
			self.xvel *= -1
		if self.rect.y <= 0 or self.rect.y > screen.get_height() - self.scale:
			self.yvel *= -1
	def grow(self):
		self.scale+=1
		self.image = pygame.transform.scale(pic, (self.scale,self.scale))
		self.update()
	def blow(self):
		if self.scale>2:
			self.xvel=random.randint(-5, 5)
			self.yvel=random.randint(-5, 5)
			self.scale-=1
			self.image = pygame.transform.scale(pic, (self.scale,self.scale))
			self.update()
		else:
			spritelist.remove(self)
while going:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			going = False
		if event.type == pygame.MOUSEBUTTONDOWN:
			mouse=True
		if event.type == pygame.MOUSEBUTTONUP:
			mouse=False
	screen.fill(black)
	spritelist.update()
	spritelist.draw(screen)
	clock.tick(60)
	pygame.display.update()
	if mouse:
		if len(spritelist)>0:
				for sprite in spritelist:
					sprite.grow()
		else:
			newSmiley = Smiley(pygame.mouse.get_pos(), 0, 0)
			spritelist.add(newSmiley)
			newSmiley.grow()
	else:
		for sprite in spritelist:
			sprite.blow()
pygame.quit()
