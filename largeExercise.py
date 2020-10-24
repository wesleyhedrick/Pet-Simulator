class Pet:
    def __init__(self, name, fullness=50, happiness=50, hunger=5, mopiness=5):
        self.name = name
        self.fullness = fullness
        self.happiness = happiness
        self.hunger = hunger
        self.mopiness = mopiness

    def eat_food(self):
        self.fullness += 30

    def get_love(self):
        self.happiness += 30

    def be_alive(self):
        self.fullness -= self.hunger
        self.happiness -= self.mopiness

        
class CuddlyPet(Pet):
    def __init__(self, name, fullness=50, hunger=5, happiness=100, cuddle_level=1, mopiness=1):
        self.name = name
        self.cuddle_level = cuddle_level
    
    def be_alive(self):
        self.fullness -= self.hunger
        self.happiness -= self.mopiness/2
        
    def cuddle(self, other_pet):
        # Super cuddle powers, activate!
        for i in range(self.cuddle_level):
            other_pet.get_love()

    


