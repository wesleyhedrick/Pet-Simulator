import json
from data import toy_effects_data


# toy_effects_data = {
#     'Lizard': {
#         'string': {
#             'mood': 60, 
#             'fullness': -10,
#             'rested': -10,
#             'hydrated': -10,
#             'life': -10
#         },
#         'ball': {
#             'mood': 60, 
#             'fullness': -10,
#             'rested': -10,
#             'hydrated': -10,
#             'life': -10
#         },
#         'rope': {
#             'mood': 60, 
#             'fullness': -10,
#             'rested': -10,
#             'hydrated': -10,
#             'life': -10
#         },
#         'feather': {
#             'mood': 60, 
#             'fullness': -10,
#             'rested': -10,
#             'hydrated': -10,
#             'life': -10
#         }
#     },
#     'Dog': {
#         'string': {
#             'mood': 60, 
#             'fullness': -10,
#             'rested': -10,
#             'hydrated': -10,
#             'life': -10
#         },
#         'ball': {
#             'mood': 60, 
#             'fullness': -10,
#             'rested': -10,
#             'hydrated': -10,
#             'life': -10
#         },
#         'rope': {
#             'mood': 60, 
#             'fullness': -10,
#             'rested': -10,
#             'hydrated': -10,
#             'life': -10
#         },
#         'feather': {
#             'mood': 60, 
#             'fullness': -10,
#             'rested': -10,
#             'hydrated': -10,
#             'life': -10
#         }
#     }, 
#     'Cat': {
#         'string': {
#             'mood': 60, 
#             'fullness': -10,
#             'rested': -10,
#             'hydrated': -10,
#             'life': -10
#         },
#         'ball': {
#             'mood': 60, 
#             'fullness': -10,
#             'rested': -10,
#             'hydrated': -10,
#             'life': -10
#         },
#         'rope': {
#             'mood': 60, 
#             'fullness': -10,
#             'rested': -10,
#             'hydrated': -10,
#             'life': -10
#         },
#         'feather': {
#             'mood': 60, 
#             'fullness': -10,
#             'rested': -10,
#             'hydrated': -10,
#             'life': -10
#         }
#     }, 
#     'Bird': {
#         'string': {
#             'mood': 60, 
#             'fullness': -10,
#             'rested': -10,
#             'hydrated': -10,
#             'life': -10
#         },
#         'ball': {
#             'mood': 60, 
#             'fullness': -10,
#             'rested': -10,
#             'hydrated': -10,
#             'life': -10
#         },
#         'rope': {
#             'mood': 60, 
#             'fullness': -10,
#             'rested': -10,
#             'hydrated': -10,
#             'life': -10
#         },
#         'feather': {
#             'mood': 60, 
#             'fullness': -10,
#             'rested': -10,
#             'hydrated': -10,
#             'life': -10
#         }
#     }
# }

with open('jsonDumpFile.py', 'w') as f:
    json.dump(toy_effects_data, f)

with open('jsonDumpFile.py', 'r') as f:
    petdata = json.load(f)

print(type(petdata))
petdata['Hamster'] = {'string': {'mood': 20, 'fullness': -2, 'rested': -2, 'hydrated': -2, 'life': -2},
                'ball': {'mood': 60, 'fullness': -10, 'rested': -10, 'hydrated': -10, 'life': -10}, 
                'rope': {'mood': 20, 'fullness': -2, 'rested': -2, 'hydrated': -2, 'life': -2}, 
                'feather': {'mood': 20, 'fullness': -2, 'rested': -2, 'hydrated': -2, 'life': -2}},

print(petdata)

with open('jsonDumpFile.py', 'w') as f:
    json.dump(petdata, f)
    

    