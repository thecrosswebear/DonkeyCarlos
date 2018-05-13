import pygame as pg
from SpriteSheet_Functions import SpriteSheet

pg.init()

SIZE = [500,500]
BLACK = [0,0,0]
WHITE = [255,255,255]

GIRL_COORD = [(0,0,120,120), (120,0,120,120), (240,0,120,120)]

screen = pg.display.set_mode(SIZE)
pg.display.set_caption("test sprite animation")

clock = pg.time.Clock()

spriteSheet = SpriteSheet("Data/spritesheet_runner-withNumbers.png")

done = False

all_sprite_list = pg.sprite.Group()

class Girl(pg.sprite.Sprite):

	def __init__(self):
		super(Girl,self).__init__()
		self.images = self.setImages()
		self.image = self.setImage()
		self.rect = self.image.get_rect()
		self.rect.x = 300
		self.rect.y = 300
		self.currentImage = 0

	def setImages(self):
		images = spriteSheet.imgsat(GIRL_COORD)
		return images

	def setImage(self):
		return self.images[0]

	def update(self):
		self.rect.x = self.rect.x - 1
		pos = self.rect.x
		frame = (pos/14) % len(self.images)
		print "frame: ", frame
		self.image = self.images[frame]

girl = Girl()
all_sprite_list.add(girl)

while not done:
	screen.fill(BLACK)

	for event in pg.event.get():
		if event.type == pg.QUIT:
			done = True

	keys = pg.key.get_pressed()
	if keys[pg.K_ESCAPE]:
		done = True

	all_sprite_list.draw(screen)
	all_sprite_list.update()
	#pg.draw.rect(screen, WHITE,(25,25,25,25))
	pg.display.update()

pg.quit()



