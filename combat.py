from turtle import speed
import pygame
import sys

pygame.init()

size = height, width = 800, 600

step = 200

black = 0,0,0

moves = 5



screen = pygame.display.set_mode(size)

character = pygame.image.load("rpg/character.jpg")
char_rect = character.get_rect()
enemy = pygame.image.load("rpg/enemy.jpg")
enemy_rect = enemy.get_rect()
enemy_rect = enemy_rect.move(600,400)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
             sys.exit()
    pygame.time.delay(10)

    char_x, char_y = 0,0

    for event in pygame.event.get():
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                char_x -= step
                moves -= 1
            if event.key == pygame.K_RIGHT:
                char_x += step
                moves -= 1
            if event.key == pygame.K_UP:
                char_y -= step
                moves -= 1
            if event.key == pygame.K_DOWN:
                char_y += step
                moves -= 1

    char_rect = char_rect.move(char_x,char_y)
    
    
    screen.fill(black)
    screen.blit(character, char_rect)
    screen.blit(enemy,enemy_rect)
    pygame.display.flip()