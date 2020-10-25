import pickle
from pets import Pet, Dog, Cat, Lizard, Bird, classDictionary
from toys import Toy

list_of_active_pets = []
list_of_active_toys = []

game_on = True

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

toy_menu = [
    'string', 
    'ball', 
    'feather',
    'rope'
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
    choices_string += f'Pick one (1-{len(menu)})\n'
    return choices_string

def render_toy_menu(menu):
    choices_string = '\n'
    for num, choice in enumerate(menu):
        choices_string += f'{num+1}. {choice}\n'
    choices_string += f'\nPick one (1-{len(menu)})\n'
    return choices_string
def render_active_toys(toys):
    choices_string = '\n'
    
def render_active_pets(active_pets):
    num_pets = len(active_pets)
    print(f'You have {num_pets} pets.\n')
    active_pets_string = ''
    for num, i in enumerate(active_pets):
        active_pets_string += f'{num+1}. {i.name}\n'
    active_pets_string += f'\nWhich one needs food?\nChoose 1-{len(active_pets)}.\n'
    return active_pets_string

def load_data():
    global list_of_active_pets
    with open('pet_list.py', 'rb') as f:
        list_of_active_pets = pickle.load(f)
        

def save_data(list_of_pets):
    with open('pet_list.py', 'wb') as f:
        pickle.dump(list_of_active_pets, f)

def present_options():
    global game_on

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
        if list_of_active_pets:       
            pet_count = len(list_of_active_pets)            
            if pet_count < 2:
                print(f'{list_of_active_pets[0].name} is feeling nice and full now.')
            else:
                
                choice = int(input(render_active_pets(list_of_active_pets)))
                choice -= 1
                list_of_active_pets[choice].fullness = 100
                the_pet_you_just_fed = list_of_active_pets[choice].name
                print(f'{the_pet_you_just_fed} is feeling nice and full now!')

        else:
            print('You don\'t have any pets yet. Adopt one!')

        # print(len(list_of_active_pets))
        # for i in range(len(list_of_active_pets)):
        #     print(list_of_active_pets[i-1].name)
        # print(choice)
        # print(choice - 1)
        # print(list_of_active_pets[choice - 1].name)

        # print(f'{list_of_active_pets[choice-1].name} is feeling full!')
    elif choice == 3:
        if list_of_active_toys: 
            print(f'You have {len(list_of_active_toys)} toys.')

            choice = int(input(render_active_toys(list_of_active_toys)))

            #if choice == 1:
                int(input('W'))
            #else:


        else: 
            print('You don\'t have any toys. Would you like to purchase one?')
            choice = int(input(render_toy_menu(toy_menu)))
            choice -= 1
            type_of_toy = toy_menu[choice]
            new_toy_instance = Toy(type_of_toy)
            list_of_active_toys.append(new_toy_instance)


            
    else:
        game_on = False


load_data()

while game_on:
    present_options()

save_data(list_of_active_pets)


