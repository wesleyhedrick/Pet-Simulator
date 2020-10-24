import json
from pets import Pet, Dog, Cat, Lizard, Bird, classDictionary

main_menu = [
    'Adopt a Pet',
    'Feed your pet',
    'Play with your pet'
]

owner_menu = [
    'Feed your pet', 
    'Play with your pet'
]

pets = [
    'Bird',
    'Cat',
    'Dog',
    'Lizard'
]


def valueErrorFunction(num):
    print(f'Please select a number between 1 and {num}\n\n')
    render_menu(main_menu)

def render_pets_menu(pets):
    pets_menu = ''
    for num, pet in enumerate(pets):
        pets_menu += f'{num+1}. {pet}\n'
    pets_menu += f'Pick a pet 1 - {len(pets)}\n'
    return pets_menu

def render_menu(menu):
    choices_string = ''
    for num, choice in enumerate(menu):
        choices_string += f'{num+1}. {choice}\n'
    choices_string += f'Pick one (1-{len(menu)})'
    return choices_string

def render_active_pets(active_pets):
    active_pets_string = ''
    for num, i in enumerate(active_pets):
        active_pets_string += f'{num+1}. {i.name}\n'
    active_pets_string += f'Which one needs food?\nChoose 1-{len(active_pets)}'
    return active_pets_string

def save_data():
    with open('pet_list.py', 'r') as f:
            data = json.load(f)
            length_of_saved_pets = len(data)

    with open('pet_list.py', 'w') as f:
        data[length_of_saved_pets] = {
            "kind": pet_subclass, 
            "name": new_pet_instance.name, 
            "fullness": new_pet_instance.fullness,
            "rested": new_pet_instance.rested,
            "hydrated": new_pet_instance.hydrated,
            "mood": new_pet_instance.mood
        }
        json.dump(data, f)


def present_options():
    
    choice = int(input(render_menu(main_menu)))

    if choice == 1:
        #Congratulate the customer
        #Ask customer what kind of pet by rendering pet menu
        print('You\'re going somebody very happy today!\n')
        kind = int(input(render_pets_menu(pets)))

        # Ask what the name of the pet will be
        kind -= 1
        pet_name = input(f'What would you like to name your {pets[kind]}\n').lower()
        print(pet_name)
        
        #this dynamically generates the class name so that later that class can be created without if statements
        pet_subclass = pets[kind]
        print(pet_subclass)

        #instantiate a new pet dynamically of the kind chosen by the customer and with customer-chosen name
        new_pet_instance = classDictionary[pet_subclass](pet_name.capitalize())
        
        #Append this new pet to the list of active pets
        list_of_active_pets.append(new_pet_instance)
        
        print(f'You\'re the proud new owner of {new_pet_instance.name} the cutest {str(pet_subclass).lower()}.')
        

    elif choice == 2:
        with open('pet_list.py', 'r') as f:
                data = json.load(f)
                length_of_saved_pets = len(data)
                if length_of_saved_pets

        if list_of_active_pets or length_of_saved_pets:       
            pluralsingularpet = 'pets' if length_of_saved_pets > 1 else 'pet'
            print(f'You have {length_of_saved_pets} {pluralsingularpet}.')
            choice = int(input(render_active_pets(list_of_active_pets)))
            list_of_active_pets[choice-1].fullness = 100
        
        print(len(list_of_active_pets))
        for i in range(len(list_of_active_pets)):
            print(list_of_active_pets[i-1].name)
        print(choice)
        print(choice - 1)
        print(list_of_active_pets[choice - 1].name)

        print(f'{list_of_active_pets[choice-1].name} is feeling full!')

list_of_active_pets = []

while True:
    present_options()


