from .temp_container import TempContainer
from movements import IDigging, ISlithering

class Sandbox(TempContainer):
   
    def __init__(self, name):
        super().__init__(name)

    # Duck typing check
    def add_digger_pythonic(self, animal):
        try:
            if animal.dig_speed > -1:
                self.animals.add(animal)
        except AttributeError as ex:
            print(f'{animal} doesn\'t like to dig, so please do not try to put it in the {self.name} container')

    # Actual typing check
    def add_digger_type_check(self, animal):
        if isinstance(animal, IDigging):
            self.animals.add(animal)
        elif isinstance(animal, ISlithering):
            print(f'{animal} is a snake! It doesn\'t belong in this container.')
        else:
            print(f'{animal} doesn\'t like to dig, so please do not try to put it in the {self.name} container')