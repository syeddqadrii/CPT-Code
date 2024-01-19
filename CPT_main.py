"""
Name: Syed Qadri
Date: January 12, 2024
Program: Maze Game - CPT Program
Course: ICS3U1
"""

# Import PyGame
import pygame

# Other Imports
from CPT_Class import Button  # Import Button Class
from tkinter import messagebox  # Import Message Box

# Initiate PyGame
pygame.init()
pygame.mixer.init()

# Surface
surface = pygame.display.set_mode([1200, 720])  # Main Surface
pygame.display.set_caption("SQ PRODUCTIONS™ Presents Maze Game")  # Window Caption
pygame.display.set_icon(pygame.image.load('images/maze_icon.png'))  # Window Icon

# Program Start-Up Screen
pygame.mixer.music.load('audio/start_sound.mp3')  # Load Start-Up Sound
start_screen = pygame.image.load('images/Loading Screen.jpg')  # Loading Screen Image
surface.blit(start_screen, (0, 0))  # Blit Loading Screen
pygame.display.update()  # Update The Screen
pygame.mixer.music.play()  # Play Start-Up Sound
pygame.time.wait(4500)  # Loading Screen Time

# Load Images
start_trigger = pygame.image.load('images/start_trigger.jpg')  # Start trigger Image
menu_screen = pygame.image.load("images/main_menu.jpg")  # Menu Screen Background
instruction_screen = pygame.image.load('images/instruction_screen.jpg')
play_image = pygame.image.load('images/play_button_up.jpg')  # Play Image (rest)
play_image2 = pygame.image.load('images/play_button_down.jpg')  # Play Image (hover)
instr_image = pygame.image.load('images/instructions_button_up.jpg')  # Instruction Image (rest)
instr_image2 = pygame.image.load('images/instructions_button_down.jpg')  # Instruction Image (hover)
quit_image = pygame.image.load('images/quit_button_up.jpg')  # Quit Image (rest)
quit_image2 = pygame.image.load('images/quit_button_down.jpg')  # Quit Image (hover)
return_image = pygame.image.load('images/return_button_up.jpg')  # Return Image (rest)
return_image2 = pygame.image.load('images/return_button_down.jpg')  # Return Image (hover)

# Audio Files
theme_song = pygame.mixer.Sound('audio/theme_song.mp3')  # Load Theme Song
theme_song.set_volume(0.05)  # Set Theme Song Volume


# Program Main Code
def the_maze_game():

    # Set Variables
    main_menu = True  # Main Menu
    start_menu = False  # Start Menu
    level_1 = False  # Level 1 Variable
    level_2 = False  # Level 2 Variable
    level_3 = False  # Level 3 Variable
    level_4 = False  # Level 4 Variable
    level_5 = False  # Level 5 Variable
    instr = False

    # Game Loop Code
    while True:

        # Quitting the Program
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        # Main Menu Code
        if main_menu:

            # Create Presets
            pygame.mouse.set_visible(True)
            pygame.display.set_caption('Maze Game - Main Menu')

            # Play Music
            theme_song.play()

            # Create Menu Screen
            surface.blit(menu_screen, (0, 0))

            # Create Menu Buttons
            play_button = Button(462.5, 250, play_image, play_image2)  # Play Button
            instr_button = Button(462.5, 385, instr_image, instr_image2)  # Instruction Button
            quit_button = Button(462.5, 520, quit_image, quit_image2)  # Quit Button

            # If User Interacts with Buttons
            if play_button.draw(surface):  # Play Button
                start_menu = True
                main_menu = False

            if instr_button.draw(surface):  # Instruction Button
                main_menu = False
                instr = True

            if quit_button.draw(surface):
                pygame.quit()
                exit()

        # Instruction Screen
        elif instr:

            # Set Caption
            pygame.display.set_caption('Maze Game - Instructions')

            # Show Instructions
            surface.blit(instruction_screen, (0, 0))

            # Create Return Button
            return_button = Button(900, 600, return_image, return_image2)

            # If User Wishes to Return
            if return_button.draw(surface):  # Show Return Button
                main_menu = True
                instr = False

        # Start Menu Code
        elif start_menu:

            # Stop Main Theme
            pygame.mixer.stop()

            # Reset and Customize Screen
            surface.fill("black")
            pygame.display.set_caption('The Maze Game - Start')

            # Set X and Y
            st_x = 60
            st_y = 560

            # Start trigger Code
            start_trigger_rect = start_trigger.get_rect()  # Get Start Trigger Rect
            pos = pygame.mouse.get_pos()  # Get Mouse Pos
            start_trigger_rect.topleft = (st_x, st_y)  # Set Rect Spawn
            surface.blit(start_trigger, (st_x, st_y))  # Blit Trigger

            # Check if mouse is colliding with the start trigger
            if start_trigger_rect.collidepoint(pos):
                level_1 = True
                start_menu = False

        # Level 1 Code
        elif level_1:

            # Reset and Customize Screen
            pygame.display.set_caption("Level 1 - The Maze Game")
            surface.fill('#FF0048')
            pygame.mouse.set_visible(False)

            # Create Mouse Sprite
            mouse_rect = pygame.Rect(0, 0, 10, 10)
            pos = pygame.mouse.get_pos()
            mouse_rect.center = pos

            # Create Level One Finish Box
            finish_rect = pygame.Rect(1050, 25, 100, 100)

            # Create Walls
            walls_1 = [
                pygame.Rect(0, 0, 60, 720),
                pygame.Rect(60, 0, 550, 560),
                pygame.Rect(0, 660, 1200, 500),
                pygame.Rect(0, 0, 1200, 25),
                pygame.Rect(750, 125, 1200, 700),
                pygame.Rect(1150, 0, 50, 720),
            ]

            # Blit All Sprites on Screen
            for wall in walls_1:
                pygame.draw.rect(surface, 'black', wall)  # Blit Walls
            pygame.draw.rect(surface, "#00ff9d", mouse_rect)  # Blit Mouse Sprite
            pygame.draw.rect(surface, "#00ff9d", finish_rect)  # Blit Finish Box

            # If the player hits the wall
            for wall in walls_1:
                if mouse_rect.colliderect(wall):
                    main_menu = True
                    level_1 = False

            # If the player reaches the end
            if mouse_rect.colliderect(finish_rect):
                level_2 = True
                level_1 = False

        # Level 2 Code
        elif level_2:

            # Reset and Customize Screen
            pygame.display.set_caption("Level 2 - The Maze Game")
            surface.fill('#FF0048')
            pygame.mouse.set_visible(False)

            # Create Mouse Sprite
            mouse_rect = pygame.Rect(0, 0, 10, 10)
            pos = pygame.mouse.get_pos()
            mouse_rect.center = pos

            # Create Level One Finish Box
            finish_rect = pygame.Rect(50, 620, 50, 50)

            # Create Invisible Box
            invis_rect = pygame.Rect(1050, 450, 100, 170),

            # Create Walls
            walls_2 = [
                pygame.Rect(0, 0, 1200, 25),
                pygame.Rect(1150, 0, 50, 720),
                pygame.Rect(0, 0, 50, 720),
                pygame.Rect(0, 670, 1200, 50),
                pygame.Rect(150, 125, 1200, 200),
                pygame.Rect(0, 450, 1050, 170),
            ]

            # Blit All Sprites on Screen
            for wall in walls_2:
                pygame.draw.rect(surface, 'black', wall)  # Blit Walls
            pygame.draw.rect(surface, "#00ff9d", mouse_rect)  # Blit Mouse Sprite
            pygame.draw.rect(surface, "#00ff9d", finish_rect)  # Blit Finish Box
            pygame.draw.rect(surface, "gray", invis_rect)  # Invisible Rectangle

            # If the player hits the wall
            for wall in walls_2:
                if mouse_rect.colliderect(wall):
                    main_menu = True
                    level_2 = False

            # If the player reaches the end
            if mouse_rect.colliderect(finish_rect):
                level_3 = True
                level_2 = False

        # Level 3 Code
        elif level_3:

            # Reset and Customize Screen
            pygame.display.set_caption("Level 3 - The Maze Game")
            surface.fill('#FF0048')
            pygame.mouse.set_visible(False)

            # Create Mouse Sprite
            mouse_rect = pygame.Rect(0, 0, 10, 10)
            pos = pygame.mouse.get_pos()
            mouse_rect.center = pos

            # Create Level One Finish Box
            finish_rect = pygame.Rect(585, 50, 35, 35)

            # Create Walls
            walls_3 = [pygame.Rect(0, 0, 50, 720),
                       pygame.Rect(0, 0, 1200, 50),
                       pygame.Rect(620, 0, 1200, 720),
                       pygame.Rect(250, 85, 1200, 720),
                       ]

            # Blit All Sprites on Screen
            for wall in walls_3:
                pygame.draw.rect(surface, 'black', wall)  # Blit Walls
            pygame.draw.rect(surface, "#00ff9d", mouse_rect)  # Blit Mouse Sprite
            pygame.draw.rect(surface, "#00ff9d", finish_rect)  # Blit Finish Box

            # If the player hits the wall
            for wall in walls_3:
                if mouse_rect.colliderect(wall):
                    main_menu = True
                    level_3 = False

            # If the player reaches the end
            if mouse_rect.colliderect(finish_rect):
                level_4 = True
                level_3 = False

        # Level 4 Code
        elif level_4:
            # Reset and Customize Screen
            pygame.display.set_caption("Level 4 - The Maze Game")
            surface.fill('#FF0048')
            pygame.mouse.set_visible(False)

            # Create Mouse Sprite
            mouse_rect = pygame.Rect(0, 0, 10, 10)
            pos = pygame.mouse.get_pos()
            mouse_rect.center = pos

            # Create Level One Finish Box
            finish_rect = pygame.Rect(1050, 620, 35, 35)

            # Create Invisible Box
            invis_rect_1 = pygame.Rect(650, 490, 250, 30),
            invis_rect_2 = pygame.Rect(900, 490, 250, 30),

            # Create Walls
            walls_4 = [pygame.Rect(0, 0, 1200, 50),
                       pygame.Rect(0, 0, 575, 720),
                       pygame.Rect(620, 0, 580, 490),
                       pygame.Rect(580, 520, 585, 100),
                       pygame.Rect(1000, 655, 585, 100),
                       pygame.Rect(400, 520, 650, 200),
                       ]

            # Blit All Sprites on Screen
            for wall in walls_4:
                pygame.draw.rect(surface, 'black', wall)  # Blit Walls
            pygame.draw.rect(surface, "#00ff9d", mouse_rect)  # Blit Mouse Sprite
            pygame.draw.rect(surface, "#00ff9d", finish_rect)  # Blit Finish Box
            pygame.draw.rect(surface, "gray", invis_rect_1)  # Invisible Rectangle 1
            pygame.draw.rect(surface, "gray", invis_rect_2)  # Invisible Rectangle 2

            # If the player hits the wall
            for wall in walls_4:
                if mouse_rect.colliderect(wall):
                    main_menu = True
                    level_4 = False

            # If the player reaches the end
            if mouse_rect.colliderect(finish_rect):
                level_5 = True
                level_4 = False
                
        # Level 5 Code
        elif level_5:
            # Reset and Customize Screen
            pygame.display.set_caption("Level 5 - The Maze Game")
            surface.fill('#FF0048')
            pygame.mouse.set_visible(False)

            # Create Mouse Sprite
            mouse_rect = pygame.Rect(0, 0, 10, 10)
            pos = pygame.mouse.get_pos()
            mouse_rect.center = pos

            # Create Level One Finish Box
            finish_rect = pygame.Rect(100, 100, 15, 15)

            # Create Walls
            walls_5 = [pygame.Rect(0, 0, 1200, 100),
                       pygame.Rect(600, 0, 1200, 620),
                       pygame.Rect(1120, 0, 180, 720),
                       pygame.Rect(0, 690, 1200, 30),
                       pygame.Rect(0, 0, 100, 720),
                       pygame.Rect(200, 500, 1000, 120),
                       pygame.Rect(0, 200, 500, 250),
                       pygame.Rect(350, 0, 500, 160),
                       pygame.Rect(275, 125, 50, 200),
                       pygame.Rect(115, 0, 130, 160),
                       pygame.Rect(150, 175, 25, 200),
                       pygame.Rect(115, 0, 10, 185),
                       ]

            # Blit All Sprites on Screen
            for wall in walls_5:
                pygame.draw.rect(surface, 'black', wall)  # Blit Walls
            pygame.draw.rect(surface, "#00ff9d", mouse_rect)  # Blit Mouse Sprite
            pygame.draw.rect(surface, "#00ff9d", finish_rect)  # Blit Finish Box

            # If the player hits the wall
            for wall in walls_5:
                if mouse_rect.colliderect(wall):
                    main_menu = True
                    level_5 = False

            # If the player reaches the end
            if mouse_rect.colliderect(finish_rect):
                level_5 = False

        # When The Game Ends
        else:

            # Show Message box
            msg_box = messagebox.askyesno('You Win!!', f'You have successfully finished the maze game.\nWould you like to play again?')

            # If player chooses to play again
            if msg_box:
                the_maze_game()

            # If player chooses to leave
            else:
                pygame.quit()
                exit()

        # Blit and Update Screen
        pygame.display.flip()
        pygame.display.update()


# Start Game Loop
the_maze_game()
