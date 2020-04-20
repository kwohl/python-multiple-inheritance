from animals import Penguin, PaintedDog, Ant, Betta, Copperhead, Earthworm, Finch, Gerbil, Mouse, Parakeet, Terrapin, TimberRattlesnake
from habitats import Habitat, Aquarium, TempContainer, Aviary, Sandbox, Snakepit, Tank

bob = Penguin("Bob")
bob.run()
bob.swim()
print()
ralph = PaintedDog("Ralph")

seaworld = Aquarium("Sea World")
seaworld.add_swimmer_pythonic(bob)
seaworld.add_swimmer_pythonic(ralph)
seaworld.add_swimmer_type_check(ralph)
for animal in seaworld.animals:
    print(f'{animal} lives in Sea World')

print()
# animals needing temporary containers
andy = Ant("Andy")
kristen = Betta("Kristen")
bryan = Copperhead("Bryan")
chase = Earthworm("Chase")
jisie = Finch("Jisie")
ashley = Gerbil("Ashley")
kristin = Mouse("Kristin")
john = Parakeet("John")
jeremiah = Terrapin("Jeremiah")
brenda = TimberRattlesnake("Brenda")
# temporary containers
diggers = Sandbox("Temporary Digger Home")
fliers = Aviary("Temporary Flier Home")
swimmers = Tank("Temporary Swimmer Home")
slitherers = Snakepit("Temporary Snake Home")

diggers.add_digger_type_check(andy)
diggers.add_digger_pythonic(kristen)
diggers.add_digger_type_check(brenda)
diggers.add_digger_type_check(chase)
diggers.add_digger_type_check(ashley)
diggers.add_digger_type_check(kristin)
print()
fliers.add_flier_type_check(jisie)
fliers.add_flier_pythonic(john)
fliers.add_flier_pythonic(ashley)
print()
swimmers.add_swimmer_type_check(kristen)
swimmers.add_swimmer_pythonic(jeremiah)
swimmers.add_swimmer_type_check(andy)
print()
slitherers.add_snake_pythonic(brenda)
slitherers.add_snake_type_check(bryan)
slitherers.add_snake_type_check(kristin)




