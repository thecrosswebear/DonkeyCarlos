import pygame
from SpriteSheet_Functions import SpriteSheet
from Sounds import *


pygame.init()

'''
background-position: -6px -340px; 
width: 239px;
height: 275px;
'''





SIZE = [478,550]
BLACK = [0,0,0]
SCALE_POURCENTAGE = 100
#xVectorMario = 5 #scaled at 430%
xVectorMario = 2 #not scaled

screen = pygame.display.set_mode(SIZE)
all_sprite_list = pygame.sprite.Group()
pygame.display.set_caption("Dankey Kang")
clock = pygame.time.Clock()


SPRITE_SHEET_FILE = "Data/donkey-kong-sprite-sheet-2.png"
SPRITE_SHEET = SpriteSheet(SPRITE_SHEET_FILE)

LEVEL_COORD = (6,340,239,275)
MARIO_COORD = [(10,200,20,20),(30,200,20,20), (50,200,20,20)]

def scaleImage(image, pourcentage = SCALE_POURCENTAGE):
		new_width = image.get_width() + (image.get_width() * (SCALE_POURCENTAGE/100))
		new_height = image.get_height() + (image.get_height() * (SCALE_POURCENTAGE/100))
		print "new width: ",new_width
		print "new height: ", new_height
		return pygame.transform.scale(image, (new_width, new_height)) 
		#image = pygame.transform.scale(image, (new_width, new_height)) 
		#return image

level_image = scaleImage(SPRITE_SHEET.imgat(LEVEL_COORD))		


class Mario(pygame.sprite.Sprite):
	def __init__(self):
		super(Mario, self).__init__()
		self.images = self.setImages()
		self.scaleImages(SCALE_POURCENTAGE)
		self.image = self.setImage()
		#self.image = pygame.transform.scale(self.image, (70, 84)) 
		self.rect = self.image.get_rect()
		self.rect.x = 400
		self.rect.y = 200
		self.currentImage = 0
		self.direction = "Left"
		
	def setImages(self):
			
			images = SPRITE_SHEET.imgsat(MARIO_COORD)
			return images
	
	def setImage(self):
				
		return self.images[0]

	def move(self, deplacement):
		self.rect.x += deplacement
		self.switchImage()
		#channel = mario_sounds[0].play()

	def jump(self):
		pass

	def update(self, deplacementMario):
		self.rect.x += deplacementMario
		pos = self.rect.x

		if self.direction == "Right":
			frame = (pos //3) % len(self.images)
			self.image = pygame.transform.flip(self.images[frame], True, False)
			#self.image = self.images[frame]
		else:
			frame = (pos //3) % len(self.images)
			self.image = self.images[frame]




	def switchImage(self):

		if self.currentImage == 2:
			self.currentImage = 0
		else:
			self.currentImage += 1
		
		if self.direction == "Right":
			self.image = pygame.transform.flip(self.images[self.currentImage], True, False)
		else:
			self.image = self.images[self.currentImage]

		#self.image = pygame.transform.scale(self.image, (70, 84)) 

	#print "test tableau", mario.images[0].get_rect().get_width()
	#print "test tableau", mario.images[0].get_width()
	def scaleImages(self, pourcentage = SCALE_POURCENTAGE):
		for i in range(0, len(self.images)):
			new_width = self.images[i].get_width() + (self.images[i].get_width() * (SCALE_POURCENTAGE/100))
			new_height = self.images[i].get_height() + (self.images[i].get_height() * (SCALE_POURCENTAGE/100))

			self.images[i] = pygame.transform.scale(self.images[i], (new_width, new_height)) 
        
	


done = False

mario = Mario()
print("len de mario: "), len(mario.images)
all_sprite_list.add(mario)

while not done:
	screen.fill(BLACK)
	screen.blit(level_image, (0,0))

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
		if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					print "left"
					#mario.direction = "Left"
					#mario.move(-xVectorMario)
				else:
					print "right"
					#mario.direction = "Right"
					#mario.move(xVectorMario)

					#mario.
					#mario.move(-xVectorMario)
					#mario.image = mario.images[3]
					print ("mario currentImage: "), mario.currentImage

	keys = pygame.key.get_pressed()
	if keys[pygame.K_ESCAPE]:
		done = True
	
	if keys[pygame.K_LEFT]:
		mario.direction = "Left"
		#mario.move(-xVectorMario)
		mario.update(-xVectorMario)
	elif keys[pygame.K_RIGHT]:
		mario.direction = "Right"
		#mario.move(xVectorMario)
		mario.update(xVectorMario)
	elif keys[pygame.K_SPACE]:
		channel = mario_sounds[1].play()
	

	
	all_sprite_list.draw(screen)
	clock.tick(40)

	pygame.display.update()

pygame.quit()
