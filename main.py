"""
Author: Lucas Roberts
Date: 2/26/22
Description: This program is going to be the computer version of a game that was created by me and my teammates for our
Financial Planning Course Project. It will be a single player game whose aim is to teach players about saving for
retirement and Investing. As such the goal of the game is to reach a certain amount of money by the end of X turns while
managing expenses such as insurance, healthcare, rent and others.
Credit: The structure of the game loops was taken from 'baraltech' 'Menu-System-PyGame' repository
(https://github.com/baraltech/Menu-System-PyGame/blob/main/button.py)
from the video they used on their YouTube (https://www.youtube.com/watch?v=GMBqjxcKogA)
"""

import pygame
import sys
from button import Button
from player import Player

# Initializing needed variables
running = True
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
ORIGIN = (0, 0)

# Initializes pygame
pygame.init()
SCREEN_SIZE = SCREEN_HEIGHT, SCREEN_WIDTH = 1280, 720
clock = pygame.time.Clock()
flags = pygame.SCALED | pygame.RESIZABLE

SCREEN = pygame.display.set_mode(SCREEN_SIZE, flags=flags)
pygame.display.set_caption("Menu")

BG = pygame.image.load("assets/Menu_Background.png").convert_alpha()
BG = pygame.transform.scale(BG, SCREEN_SIZE)


def set_player_info(player_amount):
    # Creating player instances to track balances and job info
    # TODO 1: Make this if statement more efficient, I feel like its so bulky
    if player_amount == 1:
        player_1 = Player()
        job_progression = player_1.get_new_income()
        print(player_1.job)
        player_income = player_1.job[job_progression]
        print(f"The starting age for Player 1 is {player_1.age} and the job is {player_1.job['Job Title']}")
        print(f"The Player 1's income is {player_income}")
    elif player_amount == 2:
        player_1 = Player()
        player_2 = Player()
        job_progression = player_1.get_new_income()
        player_1_income = player_1.job[job_progression]
        job_progression = player_2.get_new_income()
        player_2_income = player_2.job[job_progression]
        print(f"The starting age for Player 1 is {player_1.age} and the job is {player_1.job['Job Title']}")
        print(f"The Player 1's income is {player_1_income}")
        print("\n")
        print(f"The starting age for Player 2 is {player_2.age} and the job is {player_2.job['Job Title']}")
        print(f"The Player 2's income is {player_2_income}")
    elif player_amount == 3:
        player_1 = Player()
        player_2 = Player()
        player_3 = Player()
        job_progression = player_1.get_new_income()
        player_1_income = player_1.job[job_progression]
        job_progression = player_2.get_new_income()
        player_2_income = player_2.job[job_progression]
        job_progression = player_3.get_new_income()
        player_3_income = player_3.job[job_progression]
        print(f"The starting age for Player 1 is {player_1.age} and the job is {player_1.job['Job Title']}")
        print(f"The Player 1's income is {player_1_income}")
        print("\n")
        print(f"The starting age for Player 2 is {player_2.age} and the job is {player_2.job['Job Title']}")
        print(f"The Player 2's income is {player_2_income}")
        print("\n")
        print(f"The starting age for Player 3 is {player_3.age} and the job is {player_3.job['Job Title']}")
        print(f"The Player 3's income is {player_3_income}")


def get_font(size):
    return pygame.font.Font("assets/font.ttf", size)


def play(players):
    players = players
    set_player_info(players)
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("black")
        pygame.display.set_caption("Retirement Reality")

        PLAY_TEXT = get_font(45).render("This is the PLAY screen.", True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()


def player_selector():
    while True:
        PLAY_SELECTION_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("#585d66")

        PLAY_TEXT = get_font(45).render("Select how many players are playing.", True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        PLAY_BACK = Button(image=None, pos=(640, 600),
                           text_input="BACK", font=get_font(35), base_color="White", hovering_color="Green")

        ONE_PLAYER = Button(image=None, pos=(400, 460),
                            text_input="1 Player", font=get_font(35), base_color="White", hovering_color="Green")

        TWO_PLAYER = Button(image=None, pos=(640, 460),
                            text_input="2 Player", font=get_font(35), base_color="White", hovering_color="Green")

        THREE_PLAYER = Button(image=None, pos=(880, 460),
                              text_input="3 Player", font=get_font(35), base_color="White", hovering_color="Green")

        # FOUR_PLAYER = Button(image=None, pos=(640, 460),
        #                    text_input="4 Player", font=get_font(35), base_color="White", hovering_color="Green")

        for button in [PLAY_BACK, ONE_PLAYER, TWO_PLAYER, THREE_PLAYER]:
            button.changeColor(PLAY_SELECTION_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_SELECTION_MOUSE_POS):
                    main_menu()
                if ONE_PLAYER.checkForInput(PLAY_SELECTION_MOUSE_POS):
                    play(1)
                if TWO_PLAYER.checkForInput(PLAY_SELECTION_MOUSE_POS):
                    play(2)
                if THREE_PLAYER.checkForInput(PLAY_SELECTION_MOUSE_POS):
                    play(3)

        pygame.display.update()


def description():
    while True:
        DESCRIPTION_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("white")
        pygame.display.set_caption("Help")

        def text_blob():
            DESCRIPTION_TEXT_1 = get_font(25).render("The goal of this game is to save $1,000,000 by retirement age",
                                                     True, "Black")
            DESCRIPTION_RECT_1 = DESCRIPTION_TEXT_1.get_rect(center=(640, 180))
            SCREEN.blit(DESCRIPTION_TEXT_1, DESCRIPTION_RECT_1)

            DESCRIPTION_TEXT_2 = get_font(25).render("This is done through careful saving, spending, and investing "
                                                     "habits", True, "Black")
            DESCRIPTION_RECT_2 = DESCRIPTION_TEXT_2.get_rect(center=(640, 220))
            SCREEN.blit(DESCRIPTION_TEXT_2, DESCRIPTION_RECT_2)

            DESCRIPTION_TEXT_3 = get_font(25).render("You will get to choose 1 of 3 randomly selected jobs & incomes"
                                                     " and a starting age", True, "Black")
            DESCRIPTION_RECT_3 = DESCRIPTION_TEXT_3.get_rect(center=(640, 260))
            SCREEN.blit(DESCRIPTION_TEXT_3, DESCRIPTION_RECT_3)
            DESCRIPTION_TEXT_4 = get_font(25).render("Each turn will force you to make important financial decisions "
                                                     "that will affect your future", True, "Black")
            DESCRIPTION_RECT_4 = DESCRIPTION_TEXT_4.get_rect(center=(640, 300))
            SCREEN.blit(DESCRIPTION_TEXT_4, DESCRIPTION_RECT_4)

            DESCRIPTION_TEXT_5 = get_font(25).render("Try to save enough money to retire with the resources give"
                                                     " to you", True, "Black")
            DESCRIPTION_RECT_5 = DESCRIPTION_TEXT_5.get_rect(center=(640, 340))
            SCREEN.blit(DESCRIPTION_TEXT_5, DESCRIPTION_RECT_5)

        text_blob()
        OPTIONS_BACK = Button(image=None, pos=(640, 460),
                              text_input="BACK", font=get_font(75), base_color="Black", hovering_color="Green")

        OPTIONS_BACK.changeColor(DESCRIPTION_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(DESCRIPTION_MOUSE_POS):
                    main_menu()

        pygame.display.update()


def main_menu():
    while True:
        SCREEN.blit(BG, ORIGIN)
        pygame.display.set_caption("Menu")
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("Retirement Reality", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("assets/Play_Rect.png"), pos=(640, 250), text_input="PLAY",
                             font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        DESCRIPTION_BUTTON = Button(image=pygame.image.load("assets/Description_Rect.png"), pos=(640, 400),
                                    text_input="How To Play", font=get_font(75), base_color="#d7fcd4",
                                    hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Play_Rect.png"), pos=(640, 550),
                             text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, DESCRIPTION_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    player_selector()
                if DESCRIPTION_BUTTON.checkForInput(MENU_MOUSE_POS):
                    description()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()


main_menu()
