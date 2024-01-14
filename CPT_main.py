'''
Name: Syed Qadri
Date: January 12, 2024
Program: Maze Game - CPT Program
Course: ICS3U1
'''

#import
import pygame
from CPT_Class import Button

#init
pygame.init()
pygame.mixer.init()

#surface - original
surface = pygame.display.set_mode([1200, 720])  # Main Surface
pygame.display.set_caption("SQ PRODUCTIONS™ Presents Maze Game")  # Window Caption
pygame.display.set_icon(pygame.image.load('images/maze_icon.png'))  # Window Icon

#start up screen
pygame.mixer.music.load('start_sound.mp3') #Start Music
start_screen = pygame.image.load('images/Loading Screen.jpg')
surface.blit(start_screen, (0, 0))
pygame.display.update()
pygame.mixer.music.play() #Play Music
pygame.time.wait(4500)

#main menu
def main_menu():
    while True:
        pygame.display.set_caption('Maze Game - Main Menu')

        # Quitting the Program
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        menu_screen = pygame.image.load("images/main_menu.jpg")
        surface.blit(menu_screen, (0, 0))

        #pygame.draw.rect(surface, 'red', (462.5, 250, 275, 85))
        #pygame.draw.rect(surface, 'blue', (462.5, 385, 275, 85))
        #pygame.draw.rect(surface, 'green', (462.5, 520, 275, 85))
        play_image = pygame.image.load('images/play_button_up.jpg')
        play_image2 = pygame.image.load('images/play_button_down.jpg')
        play_button = Button(462.5, 250, play_image, play_image2)
        if play_button.draw(surface):
            print("START")


        pygame.display.flip()
        pygame.display.update()

        # Quitting the Program
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

main_menu()

