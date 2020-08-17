
import pygame

pygame.mixer.init()

#pygame.init()                                               # essa inicialização nos meus testes, não foi necessária

pygame.mixer.music.load('21musicateste.mp3')

pygame.mixer.music.play()

pygame.mixer.music.set_volume(1)

x = input('digite algo para encerrar ...')