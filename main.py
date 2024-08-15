# Importing Libraries.

import pygame
from pygame.locals import *   # To interact using input devices
import sys                    # Interact with python runtime environment.

# Initializing Game

pygame.init()

# Defining the window dimensions

window_width = 900
window_height = 500


# Creating game window

window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Pong Game")

# Creating Game Objects

# Defining colors

black = (0,0,0)
white = (255,255,255)

# Paddle dimension

paddle_width = 10
paddle_height = 60

# Creating paddle

paddle1 = pygame.Rect(50, 150, paddle_width, paddle_height)
paddle2 = pygame.Rect(window_width - 50, window_height - 150, paddle_width, paddle_height)

# Creating ball

ball = pygame.Rect(window_width//2 - 10, window_height//2 - 10, 20, 20)

# ball speed
ball_speed_x = 4
ball_speed_y = 4

# Game Logic

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
           pygame.quit()
           sys.exit()
           
    # Moving paddle.
    keys = pygame.key.get_pressed()
    if keys[K_w] and paddle1.y>0:
        paddle1.y -=5
    
    if keys[K_s] and paddle1.y<window_height - paddle_height:
        paddle1.y += 5
    if keys[K_UP] and paddle2.y>0:
        paddle2.y -= 5
    if keys[K_DOWN] and paddle2.y<window_height - paddle_height:
        paddle2.y += 5
        
    # Moving ball
    ball.x += ball_speed_x
    ball.y += ball_speed_y
    
    # Ball collision with bat
    if ball.colliderect(paddle1) or ball.colliderect(paddle2):
        ball_speed_x *= -1 

    # Ball collision with edges
    if ball.y < 0 or ball.y > window_height - 20:
        ball_speed_y *= -1
    if ball.x < 0:
        ball.x = window_width//2 - 10
        ball.y = window_height//2 - 10
        ball_speed_x *= -1
    if ball.x > window_width - 20:
        ball.x = window_width//2 - 10
        ball.y = window_height//2 - 10
        ball_speed_x *= -1

    # Drawing Game Objects

    # Clear the screen 
    window.fill(black)

    # Draw Paddles

    pygame.draw.rect(window, white, paddle1)
    pygame.draw.rect(window, white, paddle2)

    # Draw the ball 

    pygame.draw.ellipse(window, white, ball)

    # Update the display

    pygame.display.update()
    pygame.time.Clock().tick(60)