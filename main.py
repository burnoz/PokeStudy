import pygame
from modules.pokemon import Pokemon
from modules.button import button
from modules.preguntas import preguntas
from random import choice, shuffle
from os import system
from time import sleep

system("clear")

pygame.init()

width = 300
height = 200

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Battle")
 
q = list(preguntas.keys())
shuffle(q)
p = []

running = False
inicio_pressed = False
back_pressed = False
win = False
lose = False
d = True
dif = 1

battle_background = pygame.image.load("images/backgrounds/battle_background.png")
pantalla_dificultad = pygame.image.load("images/backgrounds/pantalla_dificultad.png")
victory = pygame.image.load("images/backgrounds/victory.png")
defeat = pygame.image.load("images/backgrounds/defeat.png")
back_button = pygame.image.load("images/buttons/back.png")
iniciar_button = pygame.image.load("images/buttons/iniciar.png")
salir_button = pygame.image.load("images/buttons/salir.png")
restart_button = pygame.image.load("images/buttons/restart.png")
dificultad_button = pygame.image.load("images/buttons/dificultad.png")
made_by = pygame.image.load("images/text/made_by.png")
squirtle_hp = pygame.image.load("images/text/squirtle_hp.png")
charmander_hp = pygame.image.load("images/text/charmander_hp.png")

iniciar = button(75, 25, iniciar_button)
salir_menu = button(90, 100, salir_button)
salir_juego = button(90, 140, salir_button)
dificultad = button(90, 85, dificultad_button)
reiniciar = button(90, 90, restart_button)
back = button(10, 10, back_button)


while d:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            d = False

    if not back_pressed:
        screen.blit(pantalla_dificultad, (0, 0))
        lvl = pygame.image.load(f"images/backgrounds/{dif}.png")
        screen.blit(lvl, (0, 130))
        screen.blit(made_by, (90, 170))

        if dificultad.draw(screen):
            if dif == 3:
                dif = 1
            else:
                dif += 1

    if back.draw(screen):
        running = True
        d = False

    pygame.display.update()

s_hp = 0
c_hp = 0

if dif == 1:
    s_hp = 3
    c_hp = 6

elif dif == 2:
    s_hp = 2
    c_hp = 7

elif dif == 3:
    s_hp = 1
    c_hp = 9


squirtle_sprite = pygame.image.load("images/sprites/squirtle.png")
squirtle_fainted_sprite = pygame.image.load("images/sprites/squirtle_fainted.png")

squirtle = Pokemon("Squirtle", s_hp, False, squirtle_sprite, squirtle_fainted_sprite, 20, 110)

charmander_sprite = pygame.image.load("images/sprites/charmander.png")
charmander_fainted_sprite = pygame.image.load("images/sprites/charmander_fainted.png")

charmander = Pokemon("Charmander", c_hp, False, charmander_sprite, charmander_fainted_sprite, 170, 0)


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if not inicio_pressed:
        screen.fill((95, 162, 173))

        if iniciar.draw(screen):
            inicio_pressed = True

        if salir_menu.draw(screen):
            running = False

        screen.blit(made_by, (90, 170))

    if inicio_pressed:
        if not win and not lose:
            screen.blit(battle_background, (0, 0))
            screen.blit(squirtle.sprite, (squirtle.x, squirtle.y))
            screen.blit(charmander.sprite, (charmander.x, charmander.y))
            screen.blit(squirtle_hp, (160, 130))
            screen.blit(charmander_hp, (20, 20))
            squirtle_current_hp = pygame.image.load(f"images/text/{squirtle.hp}.png")
            charmander_current_hp = pygame.image.load(f"images/text/{charmander.hp}.png")
            
            screen.blit(charmander_current_hp, (80, 43))
            screen.blit(squirtle_current_hp, (220, 153))

            pygame.display.update()

            pregunta = choice(q)

            if pregunta not in p:
                p.append(pregunta)

            else:
                continue

            print(pregunta)
            respuesta = input("Respuesta: ")

            if respuesta in preguntas[pregunta]:
                print("\n¡Correcto!")
                charmander.lose_health()
                print("\n")

            else:
                print("\n¡Incorrecto!")
                squirtle.lose_health()
                print("\n")

        if squirtle.hp == 0:
            screen.blit(defeat, (0, 0))
            lose = True

            if reiniciar.draw(screen):
                squirtle.hp = s_hp
                charmander.hp = c_hp
                squirtle.sprite = squirtle_sprite
                p = []
                lose = False
                inicio_pressed = False
                system("clear")
                sleep(0.5)

            if salir_juego.draw(screen):
                running = False   

        elif charmander.hp == 0:
            screen.blit(victory, (0, 0))
            win = True

            if reiniciar.draw(screen):
                squirtle.hp = 3
                charmander.hp = 6
                charmander.sprite = charmander_sprite
                p = []
                win = False
                inicio_pressed = False
                sleep(0.5)

            if salir_juego.draw(screen):
                running = False

        pygame.display.update()
        
    pygame.display.update()

system("clear")