import pygame
import sys

pygame.init()
# Control the frame rate of game
clock = pygame.time.Clock()
# intializing the screen size
screenWidth, screenHeight = 1000, 700
screen = pygame.display.set_mode((screenWidth, screenHeight))
# loading background image and assigning variable.
BG = pygame.image.load("assets/background.jpg")

def draw_text(text, font, color, surface, x, y): # defining a function draw_text for drawing words on buttons that takes the following peramiteres.
    text_obj = font.render(text, True, color) # renders text
    text_rect = text_obj.get_rect() 
    text_rect.center = (x, y) # gets position
    surface.blit(text_obj, text_rect) # draws rendered text on desired position
    

# Main menu loop function
def main_menu():

    while True: # started our loop
        playButtonRect = pygame.Rect(screenWidth // 2 - 100, screenHeight // 2 - 50, 200, 100) # start button variable position

        # Iterates over every action taken by the user
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # if the event type is quitting pygame application, exit pygame and sys.
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if playButtonRect.collidepoint(pygame.mouse.get_pos()):
                    # if the event taken was a mouse click by the user, and the collidepoint is on the start button;
                    # Transition to next screen
                    secondScreen()
                    

        screen.blit(BG, (0, 0)) # Here we initialise the BG variable to set background of menu screen
        draw_text("Chess Game", pygame.font.Font(None, 60), (0, 0, 0), screen, screenWidth // 2, 100) # title drawn using draw_text function
        colourOfButton = (0, 0, 0) # addding colour of start button
        pygame.draw.rect(screen, colourOfButton, playButtonRect) # drawing start button
        # taken from existing pygame Font class
        draw_text("Start", pygame.font.Font(None, 60), (255, 0, 0), screen, screenWidth // 2, screenHeight // 2,)

        pygame.display.flip() # turns to next screen once button clicked
        clock.tick(60)

def secondScreen(): # second screen(colour choice) function
    while True: # same loop as first screen
        whiteButtonRect = pygame.Rect(screenWidth // 2 - -100, screenHeight // 2 - 50, 200, 100) # white button variable
        blackButtonRect = pygame.Rect(screenWidth // 2 - 350, screenHeight // 2 - 50, 200, 100) # black button variable
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                    if whiteButtonRect.collidepoint(pygame.mouse.get_pos()):
                        # Transition back to first main menu screen ~ (work in progress) - wont take you to main menu in final design
                        main_menu()
                    if blackButtonRect.collidepoint(pygame.mouse.get_pos()):
                        main_menu()
                        
        screen.blit(BG, (0, 0))
        draw_text("Player One, Please Choose Your Colour", pygame.font.Font(None, 60), (0, 0, 0), screen, screenWidth // 2, 100)
        colourOfButtonWhite = (255,255,255) # adding colour of white button
        colourOfButtonBlack = (0,0,0) # adding colour of black button
        pygame.draw.rect(screen, colourOfButtonWhite, whiteButtonRect) # drawing white button on screen
        pygame.draw.rect(screen, colourOfButtonBlack, blackButtonRect) # drawing black button on screen
        draw_text("White", pygame.font.Font(None, 60), (0,0,0), screen, screenWidth // 1.4, screenHeight // 2,)
        draw_text("Black", pygame.font.Font(None, 60), (255,255,255), screen, screenWidth // 4, screenHeight // 2,)
        
        pygame.display.flip() # in this instance flips back to main menu screen (for now...)
        clock.tick(60)

main_menu() # runs program
