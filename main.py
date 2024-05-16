# Example file showing a circle moving on screen
import pygame
from person import Person

# pygame setup
pygame.init()
screen = pygame.display.set_mode((600, 600))
clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill('purple')


    pygame.draw.line(screen, "black", (100, 50), (100, 330), 10)
    pygame.draw.line(screen, "black", (100, 50), (310, 50), 10)
    pygame.draw.line(screen, "black", (300, 50), (300, 120), 3)


    Person(1, screen).draw_person()
    # # Head
    # pygame.draw.circle(screen, "black", (300, 130), 20)
    # # Left arm
    # pygame.draw.line(screen, "black", (300, 150), (250, 190), 5)
    # # Right arm
    # pygame.draw.line(screen, "black", (300, 150), (350, 190), 5)
    # # Torso
    # pygame.draw.line(screen, "black", (300, 150), (300, 240), 5)
    # # Left leg
    # pygame.draw.line(screen, "black", (300, 240), (260, 300), 5)
    # # Right leg
    # pygame.draw.line(screen, "black", (300, 240), (340, 300), 5)

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()
