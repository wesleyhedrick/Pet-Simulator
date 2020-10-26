import pickle
from pets import Pet, Dog, Cat, Lizard, Bird, classDictionary
from toys import Toy

list_of_active_pets = []
list_of_active_toys = []

game_on = True

main_menu = [
    'Adopt a Pet',
    'Feed your pet',
    'Play with your pet',
    'Quit Program'
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

def render_active_toys(active_toys):
    choices_string = '\n'


def render_active_pets(active_pets):
    num_pets = len(active_pets)
    print(f'You have {num_pets} pets.\n')
    active_pets_string = ''
    for num, i in enumerate(active_pets):
        active_pets_string += f'{num+1}. {i.name}\n'
    # active_pets_string += f'\nWhich one needs food?\nChoose 1-{len(active_pets)}.\n'
    return active_pets_string

def load_pet_data():
    global list_of_active_pets
    with open('pet_list.py', 'rb') as f:
        try:
            list_of_active_pets = pickle.load(f)    
        except EOFError:
            return None
        
def load_toy_data():
    global list_of_active_toys
    with open('toy_list.py', 'rb') as f:
        try:
            list_of_active_toys = pickle.load(f)    
        except EOFError:
            return None

def adopt():
        global main_menu

        #Congratulate the customer
        #Ask customer what kind of pet by rendering pet menu
        print('\nYou\'re going somebody very happy today!\n')
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
        print(f'You\'re the proud new owner of {new_pet_instance.name} the cutest {str(pet_subclass).lower()}.\n')


def save_pet_data(list_of_pets):
    with open('pet_list.py', 'wb') as f:
        pickle.dump(list_of_active_pets, f)

def save_toy_data(list_of_toys):
    with open('toy_list.py', 'wb') as f:
        pickle.dump(list_of_active_toys, f)

def present_adoption_option():
    global game_on
    choice = input('Welcome to the pet shop. Would you like adopt a pet today? Yes or No?\n')

    if choice.lower() == 'yes' :
        adopt()
    else:
        print('Okay let us know how we can help.')
        game_on = False
    
def choose_a_toy():
    toy_choice = int(input(render_menu(toy_menu)))
    toy_choice -= 1
    toy_kind = toy_menu[toy_choice]
    new_toy_instance = Toy(toy_kind)
    list_of_active_toys.append(new_toy_instance)
    print(f'You picked {toy_kind}')
    return new_toy_instance


def present_options():

    global game_on
    global main_menu
    
    choice = int(input(render_menu(main_menu)))

    if choice == 1:
        adopt()
        
    elif choice == 2:     
        if list_of_active_pets:       
            pet_count = len(list_of_active_pets)            
            if pet_count < 2:
                print(f'{list_of_active_pets[0].name} is feeling nice and full now.\n')
            else:
                print('Which one needs food?')
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
        
        if list_of_active_pets and list_of_active_toys:
            #Please select your pet
            print('Which pet would you like to play with?')
            pet_choice = int(input(render_active_pets(list_of_active_pets)))
            pet_choice -= 1
            pet_being_played_with = list_of_active_pets[pet_choice]
            print(f'You want to play with {pet_being_played_with.name}.')
            #Please select your toy

            print('You have these toys available.')
            for num, i in enumerate(list_of_active_toys):
                print(f'{num+1}. {i.name}')
            new_or_old = int(input('Or do you want to buy a new one?\n1. Get a new one. 2. Use one of my toys.'))

            if new_or_old == 1:
                choose_a_toy()
                toy_being_played_with = len(list_of_active_toys)
                toy_being_played_with -= 1
                toy_being_played_with = list_of_active_toys[toy_being_played_with]

            else:
                print('You want to use one of your toys.')
                toy_being_played_with = int(input(render_active_toys(list_of_active_toys)))
                toy_being_played_with -= 1
                toy_being_played_with = list_of_active_toys[toy_being_played_with]

            pet_being_played_with.playwithtoy(toy_being_played_with)

        elif list_of_active_pets:
            print('You don\'t have any toys yet. You\'ll have to go to the store and pick one up!\n')
            toy_being_played_with = int(input(render_menu(toy_menu)))
            toy_being_played_with -= 1
            toy_kind = toy_menu[toy_being_played_with]
            new_toy_instance = Toy(toy_kind)

            list_of_active_toys.append(new_toy_instance)

            print(f'You picked {toy_kind}')

            print(f'Which pet would like the {toy_kind}?\n')
            pet_choice = int(input(render_active_pets(list_of_active_pets)))
            pet_choice -= 1
            pet_being_played_with = list_of_active_pets[pet_choice]

            pet_being_played_with.playwithtoy(new_toy_instance)

        else:
            print('Wait! You don’t have any pets yet! Time to adopt!') 
                              
    else:
        game_on = False


load_pet_data()
load_pet_data()

while game_on:
    if list_of_active_pets:
        present_options()
    else:
        present_adoption_option()

save_pet_data(list_of_active_pets)
save_toy_data(list_of_active_toys)


