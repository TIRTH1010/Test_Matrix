print('Testing Code spaces')

[i for i in range(10)]

import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Bouncy Ball Game')

# Set up the ball
ball_color = (255, 0, 0)
ball_radius = 20
ball_x, ball_y = width // 2, height // 2
ball_speed_x, ball_speed_y = 5, 5

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Move the ball
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # Bounce the ball off the walls
    if ball_x - ball_radius < 0 or ball_x + ball_radius > width:
        ball_speed_x = -ball_speed_x
    if ball_y - ball_radius < 0 or ball_y + ball_radius > height:
        ball_speed_y = -ball_speed_y

    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw the ball
    pygame.draw.circle(screen, ball_color, (ball_x, ball_y), ball_radius)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(60)
    # Hello World program
    def hello_world():
        print("Hello, World!")

    hello_world()

