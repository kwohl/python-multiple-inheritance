class Arrangement:

    def __init__(self):
        self.flowers = []

    def enhance(self, flower):
        self.flowers.append(flower)


class MothersDay(Arrangement):

    def __init__(self):
        super().__init__()

    def enhance(self, flower):
        if isinstance(flower, IOrganic):
            self.flowers.append(flower)
        else:
            print(f"This {flower.name} does not belong in the Mother's Day Arrangement.")

    def trim(self, length = 4):
        for flower in self.flowers:
            flower.stem_length = length
            print(f"The stem on the {flower.name} is now {flower.stem_length} inches.")

class ValentinesDay(Arrangement):
    def __init__(self):
        super().__init__()
     
    def enhance(self, flower):
        if isinstance(flower, INotOrganic):
            self.flowers.append(flower)
        else:
            print(f"This {flower.name} does not belong in the Valentine's Day Arrangement.")
    # Override the `enhance` method to ensure only
    # roses, lillies, and alstroemeria can be added

    def trim(self, length = 7):
        for flower in self.flowers:
            flower.stem_length = length
            print(f"The stem on the {flower.name} is now {flower.stem_length} inches.")

class IOrganic:

    def __init__(self):
        self.isOrganic = True

class INotOrganic:

    def __init__(self):
        self.isOrganic = False

class Flower:

    def __init__(self):
        self.stem_length = 10

class Rose(Flower, INotOrganic):
    def __init__(self):
        Flower.__init__(self)
        INotOrganic.__init__(self)
        self.name = "rose"

class Lily(Flower, INotOrganic):
    def __init__(self):
        Flower.__init__(self)
        INotOrganic.__init__(self)
        self.name = "lily"

class Alstroemeria(Flower, INotOrganic):
    def __init__(self):
        Flower.__init__(self)
        INotOrganic.__init__(self)
        self.name = "alstroemeria"

class Daisy(Flower, IOrganic):
    def __init__(self):
        Flower.__init__(self)
        IOrganic.__init__(self)
        self.name = "daisy"

class Baby_Breath(Flower, IOrganic):
    def __init__(self):
        Flower.__init__(self)
        IOrganic.__init__(self)
        self.name = "baby's breath"

class Poppy(Flower, IOrganic):
    def __init__(self):
        Flower.__init__(self)
        IOrganic.__init__(self)
        self.name = "poppy"

red_rose = Rose()
pink_rose = Rose()
white_lily = Lily()
white_daisy = Daisy()
for_beth = ValentinesDay()
for_beth.enhance(red_rose)
for_beth.enhance(pink_rose)
for_beth.enhance(white_lily)

for_beth.enhance(white_daisy)

for_beth.trim()


