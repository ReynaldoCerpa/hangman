import pygame


class Person:
    # Draw points of the person
    coordinates = [
        [(300, 130)],
        [(300, 150), (250, 190)],
        [(300, 150), (350, 190)],
        [(300, 150), (300, 240)],
        [(300, 240), (260, 300)],
        [(300, 240), (340, 300)]
    ]

    def __init__(self, chances, screen):
        self.chances = chances
        self.screen = screen

    def render(self):
        for i in range(len(self.coordinates) - self.chances):
            if i == 0:
                pygame.draw.circle(self.screen, "black", self.coordinates[i][0], 20)
            else:
                pygame.draw.line(self.screen, "black",
                             self.coordinates[i][0], self.coordinates[i][1], 5)
