from .temp_container import TempContainer
from movements import ISlithering
from animals import Mouse, Gerbil

class Snakepit(TempContainer):
   
    def __init__(self, name):
        super().__init__(name)

    # Duck typing check
    def add_snake_pythonic(self, animal):
        try:
            if animal.slither_speed > -1:
                self.animals.add(animal)
        except AttributeError as ex:
            print(f'{animal} is not a snake, so please do not try to put it in the {self.name} container')

    # Actual typing check
    def add_snake_type_check(self, animal):
        if isinstance(animal, ISlithering):
            self.animals.add(animal)
        if isinstance(animal, Mouse) or isinstance(animal, Gerbil):
            print(f'Stop! {animal} will become snake food!')
        else:
            print(f'{animal} is not a snake, so please do not try to put it in the {self.name} container')