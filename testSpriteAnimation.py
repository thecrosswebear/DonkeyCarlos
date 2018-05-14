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

	animcycle = 15

	def __init__(self):
		super(Girl,self).__init__()
		self.images = self.setImages()
		self.image = self.setImage()
		self.rect = self.image.get_rect()
		self.rect.x = 300
		self.rect.y = 300
		self.currentImage = 0
		self.counter = 0
		self.frameSpeed = 3
		self.maxcount = len(self.images)*self.animcycle

	def setImages(self):
		images = spriteSheet.imgsat(GIRL_COORD)
		return images

	def setImage(self):
		return self.images[0]

	def update(self):

		print ("self.counter avant: "), self.counter
		self.counter = (self.counter + 1) % self.maxcount
		print "(self.counter + 1) mod self.maxcount: ", self.counter
		print "frame image self.counter/self.animcycle: ", self.counter/self.animcycle
		self.image = self.images[self.counter/self.animcycle]
		
		#print "currentImage: ", self.currentImage
		#self.currentImage = self.currentImage + 1
		#print "currentImage add 1: ", self.currentImage

		#self.image = self.images[(((self.currentImage) /self.animcycle) % len(self.images))]

		#self.currentImage = (((self.currentImage) /self.animcycle) % len(self.images))
		#print "currentImage after: ", self.currentImage
		#self.image = self.images[self.currentImage]
			

		#old maniere
		#sprite.image = frame_list[current_frame] #set the current frame
    	#current_frame = (current_frame+1)%num_frames



		#self.image = self.images[self.currentImage]
		#self.currentImage = (self.currentImage +1) % len(self.images)

		#current_frame = 0 #the frame we're currently displaying
		#num_frames = 5 # number of frames in the animation

		#def update():
		#    sprite.image = frame_list[current_frame] #set the current frame

		#    current_frame = (current_frame+1)%num_frames

		
		#if (self.counter == (self.animcycle -1):
		#	currentImage = (self.currentImage + 1) % len(self.images)

		#self.counter = (self.counter + 1) % self.animcycle 

		#self.counter = (self.counter + 1) % len(self.images)
		#frame = self.counter/self.animcycle
		#self.image = self.images[frame]
        

		#frame = (pos/14) % len(self.images)
		#print "frame: ", frame
		#self.image = self.images[frame]

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
	clock.tick(60)



pg.quit()



