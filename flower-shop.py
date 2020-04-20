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
            print("This flower does not belong in the Mother's Day Arrangement.")

class ValentinesDay(Arrangement):
    def __init__(self):
        super().__init__()
     
    def enhance(self, flower):
        if isinstance(flower, Rose) or isinstance(flower, Lily) or isinstance(flower, Alstroemeria):
            self.flowers.append(flower)
        else:
            print("This flower does not belong in the Valentine's Day Arrangement.")
    # Override the `enhance` method to ensure only
    # roses, lillies, and alstroemeria can be added

    def trim(self, length = "7 inches"):
        for flower in self.flowers:
            flower.stem = length
            print(f"The stem on this {flower.name} is now {flower.stem}.")

class Flower:

    def __init__(self):
        self.stem = ""
        self.color = ""
        self.name = ""

class Rose(Flower):
    def __init__(self):
        self.is_organic = False
        self.name = "rose"

class Lily(Flower):
    def __init__(self):
        self.is_organic = False
        self.name = "lily"

class Alstroemeria(Flower):
    def __init__(self):
        self.is_organic = False
        self.name = "alstroemeria"

class Daisy(Flower):
    def __init__(self):
        self.is_organic = True
        self.name = "daisy"

class Baby_Breath(Flower):
    def __init__(self):
        self.is_organic = True
        self.name = "baby's breath"

class Poppy(Flower):
    def __init__(self):
        self.is_organic = True
        self.name = "poppy"

if __name__ == "__main__":
    for_beth = ValentinesDay()
    red_rose = Rose()

    for_beth.enhance(red_rose)

    for_beth.trim()