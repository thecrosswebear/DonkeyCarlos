import pygame
from SpriteSheet_Functions import SpriteSheet


pygame.init()

SIZE = [500,500]
BLACK = [0,0,0]
xVectorMario = 1

screen = pygame.display.set_mode(SIZE)
all_sprite_list = pygame.sprite.Group()
pygame.display.set_caption("Dankey Kang")
clock = pygame.time.Clock()


SPRITE_SHEET_FILE = "Data/donkey-kong-sprite-sheet-2.png"
SPRITE_SHEET = SpriteSheet(SPRITE_SHEET_FILE)

MARIO_COORD = [(10,200,20,24),(30,200,20,24), (50,200,20,24)]


class Mario(pygame.sprite.Sprite):
	def __init__(self):
		super(Mario, self).__init__()
		self.images = self.setImages()
		self.image = self.setImage()
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


	def switchImage(self):

		if self.currentImage == 2:
			self.currentImage = 0
		else:
			self.currentImage += 1
		
		self.image = self.images[self.currentImage]


done = False

mario = Mario()
print("len de mario: "), len(mario.images)
all_sprite_list.add(mario)

while not done:
	screen.fill(BLACK)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
		if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					#mario.
					#mario.move(-xVectorMario)
					#mario.image = mario.images[3]
					print ("mario currentImage: "), mario.currentImage

	keys = pygame.key.get_pressed()
	if keys[pygame.K_ESCAPE]:
		done = True
	if keys[pygame.K_LEFT]:
		mario.direction = "Left"
		mario.move(-xVectorMario)

	
	all_sprite_list.draw(screen)
	clock.tick(60)

	pygame.display.update()

pygame.quit()
