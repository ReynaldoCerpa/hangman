import pygame

pygame.font.init()

class Underscores:

    font = pygame.font.SysFont('Comic Sans MS', 100)

    def __init__(self, game_word, screen) -> None:
        self.game_word = game_word
        self.screen = screen

    def render(self, letters):
        response = ''
        for letter in self.game_word:
            if letter in letters:
                response += f'{letter} '
            else:
                response += '_ '

        text = self.font.render(response, False, (0, 0, 0))
        self.screen.blit(text, (90, 350))