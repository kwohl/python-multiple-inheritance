from movements import ISlithering

class TimberRattlesnake(ISlithering):

    def __init__(self, name):
        super().__init__()
        self.name = name

    def __str__(self):
        return f'{self.name} the Timber Rattlesnake'