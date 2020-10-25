import pickle

file_name = 'serializingClassesData.py'
with open(file_name, 'rb') as f:
    pickle.load(f)


print(myCar.make)