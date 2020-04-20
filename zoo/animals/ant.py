from movements import IDigging
from movements import IWalking

class Ant(IWalking, IDigging):

    def __init__(self, name):
        IDigging.__init__(self)
        IWalking.__init__(self)
        self.name = name

    def run(self):
        print(f'{self} crawls')
        
    def __str__(self):
        return f'{self.name} the Ant'