
class Underscores:
    def __init__(self, word) -> None:
        self.word = word
        self.underscore_count = len(word)

    def render(self):
        for i, letter in enumerate(self.word):
            pass