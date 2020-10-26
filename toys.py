from toy_data import toy_effects_data

class Toy:
    def __init__(self,name):
        self.thing = 'Toy'
        self.name = name
        self.life = 100

    def __str__(self):
        return f'Name {self.name}\n Life {self.life}'
    
    def played_with(self, pet, toy):
        className = str(pet.__class__.__name__)
        effects = toy_effects_data[className][toy.name]
        pet.mood += effects['mood']
        pet.fullness += effects['fullness']
        pet.rested += effects['rested']
        pet.hydrated += effects['hydrated']
        self.life += effects['life']






