import pickle

class Car:
    def __init__(self, name, make, model, year):
        self.name = name
        self.make = make
        self.model = model
        self.year = year
    

myCar = Car('Bessy', 'BMW', '325i', 2005)
myTruck = Car('Caroline', 'Chevy', 'Silverado', 2009)

car_list = []
car_list.append(myCar)
car_list.append(myTruck)

for i in car_list:
    if i.name == 'Caroline':
        i.name = 'Lizzy'

file_name = 'serializingClassesData.py'
with open(file_name, 'wb') as f:
    pickle.dump(car_list, f)

del car_list

with open(file_name, 'rb') as f:
    renewed_car_list = pickle.load(f)

for i in renewed_car_list:
    print(i.name)

    
    


