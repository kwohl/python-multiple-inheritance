from movements import ISwimming, IWalking

class Terrapin(IWalking, ISwimming):

    def __init__(self, name):
        IWalking.__init__(self)
        ISwimming.__init__(self)
        self.name = name

    def __str__(self):
        return f'{self.name} the Terrapin'