class TempContainer:

    def __init__(self, name):
        self.name = name
        self.animals = set()

    def add_animal(self, animal):
        self.animals.add(animal)
        print(f'You have added {animal} to a temporary conatiner.')

    def remove_animal(self, animal):
        self.animals.remove(animal)

    def __str__(self):
        return f'{self.name} ({len(self)} animals)'

    def __len__(self):
        return len(self.animals)