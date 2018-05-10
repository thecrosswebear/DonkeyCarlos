import pygame

#pygame.mixer.pre_init(44100, 16, 2, 4096)
pygame.init()
pygame.mixer.init(frequency=22050,size=-16,channels=4)

jump_sound = pygame.mixer.Sound("Sounds/jump.wav")
walk_sound = pygame.mixer.Sound("Sounds/walking.wav")


mario_sounds=[walk_sound, jump_sound]