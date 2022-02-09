from pets import *

class Ninja:
    def __init__(self, first_name, last_name, pet, treats, pet_food):
        self.first_name = first_name
        self.last_name = last_name
        self.pet = pet
        self.treats = treats
        self.pet_food = pet_food

    def walk(self):
        self.pet.play()

    def feed(self):
        self.pet.eat()

    def bathe(self):
        self.pet.noise()

    def attack(self):
        self.pet.kill()



billy = Snake("billy","cobra",1,60,60,"poison")
kostas = Ninja("kostas","mazarakis",billy,5,100)

kostas.attack()



# nami = Pet("nami","yorkie",1,50,50)
# kostas = Ninja("kostas","mazarakis",nami,5,100)
# kostas.feed()
# kostas.walk()
# kostas.bathe()
# print(nami.health)