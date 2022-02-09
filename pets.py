class Pet:
    def __init__(self, name, type, tricks, health, energy):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = health
        self.energy = energy
    
    def sleep(self):
        self.energy = self.energy + 25

    def eat(self):
        self.energy = self.energy + 5
        self.health = self.health + 10

    def play(self):
        self.health = self.health + 5 

    def noise(self):
        print("whoof whoof whoof")

class Snake(Pet):
    def __init__(self, name, type, tricks, health, energy,attack):
        super().__init__(name, type, tricks, health, energy)
        self.attack = attack

    def kill(self):
        print("Spits poison on the enemies face")