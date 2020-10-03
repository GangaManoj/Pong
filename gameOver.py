#step three
#added Game Over message and instructions to continue

import pygame

pygame.init()  #imports all the pygame modules

#creating the game clock
clock = pygame.time.Clock()
#setting the delay
speed = 30 #frames per second

#creating the display
display_width = 500
display_height = 300

#setting coordinates and radius for the ball
x = 100
y = 100 
radius = 10
#setting the ball in motion
#dx and dy are the distances the ball will move along either axis in each frame
dx = 3
dy = 3

#coordinates and dimensions of the paddle
paddle_x = 10
paddle_y = 10
paddle_width = 3
paddle_height = 40

#defining functions to handle paddle collision
def hit_back():
    if x + radius > display_width:
        return True
    return False

def hit_sides():
    if y - radius < 0:
        return True
    if y + radius > display_height:
        return True
    return False

def hit_paddle():
    if x - radius <= paddle_x + paddle_width and y > paddle_y and y < paddle_y + paddle_height:
        return True
    return False

def game_over():
    end_game = True
    display.fill((0,0,0)) #wiping the screen before putting up the text

    #creating fonts to print Game Over
    font_title = pygame.font.Font(None, 36)
    font_instructions = pygame.font.Font(None, 24)

    announcement = font_title.render("Game Over", True, (255,255,255))
    announcement_rect = announcement.get_rect(center = (int(display_width/2), int(display_height/2)))
    display.blit(announcement, announcement_rect) #pastes the text on announcement onto the surface announcement_rect

    #adding instructions to quit and resume
    qinstructions = font_instructions.render("Press q to Quit", True, (255,255,255))
    qinstructions_rect = qinstructions.get_rect(center = (int(display_width/2), int(display_height/1.5)))
    display.blit(qinstructions, qinstructions_rect)

    rinstructions = font_instructions.render("Press r to Resume", True, (255,255,255))
    rinstructions_rect = rinstructions.get_rect(center = (int(display_width/2), int(display_height/1.3)))
    display.blit(rinstructions, rinstructions_rect)

    pygame.display.flip() #making the text visible to the user

    #the loop waits for input to proceed
    while (end_game):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    exit()
                if event.key == pygame.K_r:
                    exit()

display = pygame.display.set_mode((display_width, display_height))  #set_mode creates the display surface by accepting the screen size and some optional flags as arguments

#setting a caption(appears on the top of the window)
pygame.display.set_caption("Let's Pong!")

#keeping the window open
while True:
    #telling the game how fast to execute, how many frames/s we need
    #pygame will never run more than 30 frames/s
    #1 frame = 1 game loop
    clock.tick(speed)

    #checking for key presses to let the paddle move continuously
    pressed_key = pygame.key.get_pressed()
    #boolean value checks if the pressed key is down or s to move down and up or w to move up
    if pressed_key[pygame.K_DOWN] or pressed_key[pygame.K_s]: 
        if paddle_y + paddle_height + 10 <= display_height:
            paddle_y += 10
    if pressed_key[pygame.K_UP] or pressed_key[pygame.K_w]:
        if paddle_y - 10 >= 0:
            paddle_y -= 10

    #checking for quit event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    #setting display colour to black
    display.fill((0,0,0))
    #updating the coordinates
    x += dx
    y += dy

    pygame.draw.circle(display, (255,255,255), (x,y), radius) #creates a circle of colour white and radius 10 at (100,100)
    pygame.draw.rect(display, (255,255,255), (paddle_x, paddle_y, paddle_width, paddle_height)) #creates the paddle

    if x < radius:
        game_over()
    if hit_back() or hit_paddle():
        dx *= -1
    if hit_sides():
        dy *= -1

    pygame.display.update() #updating the display so the new object shows up 

