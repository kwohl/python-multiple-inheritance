class Arrangement:

    def __init__(self):
        self.flowers = []

    def enhance(self, flower):
        self.flowers.append(flower)


class MothersDay(Arrangement):

    def __init__(self):
        super().__init__()

    def enhance(self, flower):
        if isinstance(flower, Daisy) or isinstance(flower, Baby_Breath) or isinstance(flower, Poppy):
            self.flowers.append(flower)
        else:
            print(f"This {flower.name} does not belong in the Mother's Day Arrangement.")

    def trim(self, length = "4 inches"):
        for flower in self.flowers:
            flower.stem = length
            print(f"The stem on this {flower.name} is now {flower.stem}.")

class ValentinesDay(Arrangement):
    def __init__(self):
        super().__init__()
     
    def enhance(self, flower):
        if isinstance(flower, IOrganic):
            self.flowers.append(flower)
        else:
            print(f"This {flower.name} does not belong in the Valentine's Day Arrangement.")
    # Override the `enhance` method to ensure only
    # roses, lillies, and alstroemeria can be added

    def trim(self, length = "7 inches"):
        for flower in self.flowers:
            flower.stem = length
            print(f"The stem on this {flower.name} is now {flower.stem}.")

class IOrganic:

    def __init__(self):
        self.isOrganic = False

class Rose(IOrganic):
    def __init__(self):
        super().__init__()
        self.name = "rose"

class Lily(IOrganic):
    def __init__(self):
        super().__init__()
        self.name = "lily"

class Alstroemeria(IOrganic):
    def __init__(self):
        super().__init__()
        self.name = "alstroemeria"

class Daisy():
    def __init__(self):
        self.is_organic = True
        self.name = "daisy"

class Baby_Breath():
    def __init__(self):
        self.is_organic = True
        self.name = "baby's breath"

class Poppy():
    def __init__(self):
        self.is_organic = True
        self.name = "poppy"

if __name__ == "__main__":
    for_beth = ValentinesDay()
    red_rose = Rose()

    for_beth.enhance(red_rose)

    for_mom = MothersDay()
    pink_rose = Rose()
    for_mom.enhance(pink_rose)

    print()

    for_beth.enhance(pink_rose)

    for_beth.trim()

    
