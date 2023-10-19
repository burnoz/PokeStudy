import pygame
from modules.pokemon import Pokemon
from modules.button import button
from random import choice
from preguntas import preguntas

pygame.init()

width = 300
height = 200

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Battle")

p = []

running = True
back_pressed = False
inicio_pressed = False

background = pygame.image.load("images/backgrounds/background.png")
back_button = pygame.image.load("images/buttons/back.png")
iniciar_button = pygame.image.load("images/buttons/iniciar.png")
salir_button = pygame.image.load("images/buttons/salir.png")
made_by = pygame.image.load("images/text/made_by.png")

iniciar = button(75, 25, iniciar_button)
salir = button(90, 100, salir_button)
back = button(10, 10, back_button)

squirtle_sprite = pygame.image.load("images/sprites/squirtle.png")
squirtle_fainted_sprite = pygame.image.load("images/sprites/squirtle_fainted.png")

squirtle = Pokemon("Squirtle", 4, False, squirtle_sprite, squirtle_fainted_sprite, 20, 110)

charmander_sprite = pygame.image.load("images/sprites/charmander.png")
charmander_fainted_sprite = pygame.image.load("images/sprites/charmander_fainted.png")

charmander = Pokemon("Charmander", 6, False, charmander_sprite, charmander_fainted_sprite, 170, 0)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if not inicio_pressed:
        screen.fill((95, 162, 173))

        if iniciar.draw(screen):
            inicio_pressed = True

        if salir.draw(screen):
            running = False

        screen.blit(made_by, (90, 170))

    if inicio_pressed:
        screen.blit(background, (0, 0))
        screen.blit(squirtle.sprite, (squirtle.x, squirtle.y))
        screen.blit(charmander.sprite, (charmander.x, charmander.y))

        if back.draw(screen):
            inicio_pressed = False
        

    pygame.display.update()
