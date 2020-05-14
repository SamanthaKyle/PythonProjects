##############################################################################################################################
# Author: Samantha L. Kyle
# Date: 27/12/19
# Title: tictactoeboard.py
##############################################################################################################################
import pygame
import random
import typing
pygame.init()
width = 600
height = 600
win = pygame.display.set_mode((width, height))

pygame.display.set_caption("TicTacToe")
third = (width - 20) /3
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 250, 30)
RED = (255, 0, 0)

win.fill(WHITE)

run = True

rectA = pygame.Rect(10, 10, third, third)
rectB = pygame.Rect(10 + third, 10, third, third)
rectC = pygame.Rect(10 + (2 * third), 10, third, third)
rectD = pygame.Rect(10, 10 + third, third, third)
rectE = pygame.Rect(10 + third, 10 + third, third, third)
rectF = pygame.Rect(10 + (2 * third), 10 + third, third, third)
rectG = pygame.Rect(10, 10 + (2 * third), third, third)
rectH = pygame.Rect(10 + third, 10 + (2 * third), third, third)
rectI = pygame.Rect(10 + (2 * third), 10 + (2 * third), third, third)
boxes = [rectA, rectB, rectC, rectD, rectE, rectF, rectG, rectH, rectI]

occupied = [False, False, False, False, False, False, False, False, False]
symbols = ["m", "m", "m", "m", "m", "m", "m", "m", "m"]

def draw_board(width : int, height : int) -> None:
    for box in boxes:
        pygame.draw.rect(win, BLACK, box, 1)

def draw_X(x: int, y : int) -> None:
    pygame.draw.line(win, GREEN, (x - third/2 + 20, y - third/2 + 20), (x + third/2 - 20, y + third/2 - 20), 3)
    pygame.draw.line(win, GREEN, (x - third/2 + 20, y + third/2 - 20), (x + third/2 - 20, y - third/2 + 20), 3)

def draw_O(x: int, y: int) -> None:
    pygame.draw.circle(win, BLUE, (x, y), int((height - 20 )/6) - 20, 3)

def place_X(i: int) -> None:
    draw_X(int(boxes[i].x + third/2), int(boxes[i].y + third/2))
    occupied[i] = True
    symbols[i] = "x"

def place_O() -> None:
    auto_choice = random.choice(boxes)
    index = boxes.index(auto_choice)
    while occupied[index]:
        auto_choice = random.choice(boxes)
        index = boxes.index(auto_choice)
    draw_O(int(auto_choice.x + third/2), int(auto_choice.y + third/2))
    occupied[index] = True
    symbols[index] = "o"

def check_Win() -> list:
    #returns tuple(bool, str, list)
    win_lists = [[0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 4, 8], [2, 4, 6]]
    win = False
    winner = "m"
    for option in win_lists:
        if symbols[option[0]] == symbols[option[1]] == symbols[option[2]]:
            winner = symbols[option[0]]
            if winner != "m":
                win = True
                winning_boxes = option
                return [win, winner, winning_boxes]
    return [win]

def display_Win() -> None:
    if check_Win()[1] == "o":
        COLOUR = RED
    else:
        COLOUR = GREEN

    for index in check_Win()[2]:
        pygame.draw.rect(win, COLOUR, (boxes[index].x, boxes[index].y, third, third))

    return False

def reset() -> None:
    win.fill(WHITE)
    draw_board()
    occupied = [False, False, False, False, False, False, False, False, False]
    symbols = ["m", "m", "m", "m", "m", "m", "m", "m", "m"]

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    draw_board(width, height)
    #key = pygame.key.get_key_pressed()
    
    if event.type == pygame.MOUSEBUTTONDOWN:
        mousePos = pygame.mouse.get_pos()

        for i in range(len(boxes)):
            if pygame.Rect(boxes[i]).collidepoint(mousePos[0], mousePos[1]):
                if occupied[i] == False:
                    place_X(i)
                    if check_Win()[0]:
                        pygame.time.delay(200)
                        display_Win()
                        pygame.time.delay(400)
                        run = False

                    if occupied.count(False) > 1:
                        place_O()
                        pygame.time.delay(300)
                        if check_Win()[0]:
                            pygame.time.delay(600)
                            display_Win()
                            pygame.time.delay(400)
                            run = False  # if i dont want replayability
    #if key == pygame.key.SPACE_BAR: #guessing syntax
        #reset()
    pygame.display.update() 
    
pygame.quit()