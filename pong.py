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

display = pygame.display.set_mode((display_width, display_height))  #set_mode creates the display surface by accepting the screen size and some optional flags as arguments

#setting a caption(appears on the top of the window)
pygame.display.set_caption("Let's Pong!")

#keeping the window open
while True:
    #telling the game how fast to execute, how many frames/s we need
    #pygame will never run more than 30 frames/s
    #1 frame = 1 game loop
    clock.tick(speed)

    #checking for quit event
    for event in pygame.event.get():
        if event.type == pygame.QUIT():
            pygame.quit()

    #setting display colour to black
    display.fill((0,0,0))
    #updating the coordinates
    x += dx
    y += dy

    pygame.draw.circle(display, (255,255,255), (x,y), radius) #creates a circle of colour white and radius 10 at (100,100)

    #setting the bounce
    #if the edge of the ball hits the left/right wall, change direction along the x-axis and if it hits the top/bottom wall, change direction along the y-axis
    if (x < radius or x > display_width - radius):
        dx *= -1
    if (y < radius) or (y > display_height - radius):
        dy *= -1

    pygame.display.update() #updating the display so the new object shows up 

