from toys import Toy
from data import toy_effects_data


class Pet:
    def __init__(self, name):
        self.name = name
        self.fullness = 100
        self.rested = 50
        self.hydrated = 100
        self.mood = 50
        self.thing = 'Pet'
        
    def __str__(self):
        return f'Mood is {self.mood}\n Fullness is {self.fullness}\n Rested is {self.rested}\n Hydrated is {self.hydrated}\n'

    def get_food(self):
        if self.fullness == 100:
            return f'You\'re {self.category} isn\'t hungry.'
        else: 
            self.fullness = 100
            return f'You\'re {self.category} is nice and full'
    
    def get_sleep(self):
        if self.rested == 100:
            return f'You\'re {self.category} is completely rested'
        else: 
            self.rested += self.rest_effect
     
    def get_water(self):
        if self.hydrated == 100:
            return f'You\'re bird is completely rested'
        else:
            return f'You\'re {self.category} is nice and full'

    def play(self):
        self.mood += self.play_effect
        self.fullness -= self.play_effect
        self.rested -= self.play_effect
        self.hydrated -= self.play_effect

    def playwithtoy(self, toy):
        toy.played_with(self, toy)
        return f'{self.name} is feeling happy now.'


class Bird(Pet):
    def __init__(self, name):
        super().__init__(name)
        self.category = 'bird'
        self.play_effect = 30
        self.rest_effect = 60
           
    def printName(self):
        return self.__class__.__name__

class Cat(Pet):
    def __init__(self, name):
        super().__init__(name)
        self.category = 'cat'
        self.play_effect = 40
        self.rest_effect = 20
        

class Dog(Pet):
    def __init__(self, name):
        super().__init__(name)
        self.category = 'dog'
        self.play_effect = 80
        self.rest_effect = 80


class Lizard(Pet):
    def __init__(self, name):
        super().__init__(name)
        self.category = 'lizard'
        self.play_effect = 10
        self.rest_effect = 60

classDictionary = {
    'Bird' : Bird, 
    'Dog': Dog, 
    'Cat': Cat, 
    'Lizard': Lizard
}
