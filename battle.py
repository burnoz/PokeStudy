import pygame
from modules.pokemon import Pokemon
from modules.button import button
from random import choice, shuffle
from preguntas import preguntas
from os import system

system("clear")

pygame.init()

width = 300
height = 200

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Battle")

q = list(preguntas.keys())
shuffle(q)
p = []

running = True
inicio_pressed = False

background = pygame.image.load("images/backgrounds/background.png")
victory = pygame.image.load("images/backgrounds/victory.png")
defeat = pygame.image.load("images/backgrounds/defeat.png")
back_button = pygame.image.load("images/buttons/back.png")
iniciar_button = pygame.image.load("images/buttons/iniciar.png")
salir_button = pygame.image.load("images/buttons/salir.png")
made_by = pygame.image.load("images/text/made_by.png")
squirtle_hp = pygame.image.load("images/text/squirtle_hp.png")
charmander_hp = pygame.image.load("images/text/charmander_hp.png")

iniciar = button(75, 25, iniciar_button)
salir = button(90, 100, salir_button)
back = button(10, 10, back_button)

squirtle_sprite = pygame.image.load("images/sprites/squirtle.png")
squirtle_fainted_sprite = pygame.image.load("images/sprites/squirtle_fainted.png")

squirtle = Pokemon("Squirtle", 3, False, squirtle_sprite, squirtle_fainted_sprite, 20, 110)

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
        screen.blit(squirtle_hp, (160, 130))
        screen.blit(charmander_hp, (20, 40))
        squirtle_current_hp = pygame.image.load(f"images/text/{squirtle.hp}.png")
        charmander_current_hp = pygame.image.load(f"images/text/{charmander.hp}.png")
        
        screen.blit(charmander_current_hp, (80, 63))
        screen.blit(squirtle_current_hp, (220, 153))

        if squirtle.hp == 0:
            print("Charmander gana")
            break   

        elif charmander.hp == 0:
            print("Squirtle gana")
            break

        pygame.display.update()

        pregunta = choice(q)

        if pregunta not in p:
            p.append(pregunta)

        else:
            continue

        print(pregunta)
        respuesta = input("Respuesta: ")

        if respuesta in preguntas[pregunta]:
            charmander.lose_health()

        else:
            squirtle.lose_health()

        
    pygame.display.update()

if squirtle.hp == 0:
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.blit(defeat, (0, 0))

        pygame.display.update()

elif charmander.hp == 0:
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.blit(victory, (0, 0))

        pygame.display.update()


# screen.blit(background, (0, 0))
# screen.blit(squirtle.sprite, (squirtle.x, squirtle.y))
# screen.blit(charmander.sprite, (charmander.x, charmander.y))
# screen.blit(squirtle_hp, (160, 130))
# screen.blit(charmander_hp, (20, 40))
# squirtle_current_hp = pygame.image.load(f"images/text/{squirtle.hp}.png")
# charmander_current_hp = pygame.image.load(f"images/text/{charmander.hp}.png")
# screen.blit(charmander_current_hp, (80, 63))
# screen.blit(squirtle_current_hp, (220, 153))

# if back.draw(screen):
#     inicio_pressed = False