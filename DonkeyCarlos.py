import pygame
from SpriteSheet_Functions import SpriteSheet

pygame.init()

SPRITE_SHEET_FILE = "Data/space_invaders_sprite_sheet.png"
SPRITE_SHEET = SpriteSheet(SPRITE_SHEET_FILE)


SIZE = [500,500]
BLACK = [0,0,0]

screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Dankey Kang")

done = False

while not done:

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True

	keys = pygame.key.get_pressed()
	if keys[pygame.K_ESCAPE]:
		done = True

	screen.fill(BLACK)

	pygame.display.update()

pygame.quit()
