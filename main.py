import pygame
import random
from person import Person
from constants import words
from underscores import Underscores

pygame.init()

screen = pygame.display.set_mode((600, 600))

clock = pygame.time.Clock()
running = True
dt = 0

found_letters = ''
chances = 6

# pick word
game_word = words[random.randrange(0, (len(words) - 1))]


while running:

    if chances == 0:
        print('You lost...')
        break
    if len(found_letters) == len(game_word):
        print('You won!')
        break

    screen.fill('blue')
    # draws hang
    pygame.draw.line(screen, "black", (100, 50), (100, 330), 10)
    pygame.draw.line(screen, "black", (100, 50), (310, 50), 10)
    pygame.draw.line(screen, "black", (300, 50), (300, 120), 3)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN and chances > 0:
            if event.unicode in game_word and event.unicode not in found_letters:
                found_letters += event.unicode
            if event.unicode in found_letters:
                pass
            else:
                chances -= 1
    
    Person(chances=chances, screen=screen).render()
    Underscores(game_word=game_word, screen=screen).render(found_letters)

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

    

pygame.quit()
