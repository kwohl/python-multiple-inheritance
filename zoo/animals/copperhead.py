from movements import ISwimming, ISlithering

class Copperhead(ISlithering, ISwimming):

    def __init__(self, name):
        ISwimming.__init__(self)
        ISlithering.__init__(self)
        self.name = name

    def __str__(self):
        return f'{self.name} the Copperhead'