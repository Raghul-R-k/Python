# watch_details = {
#     'Titan' : 8000,
#     'Titan' : 8400,
#     'Fasttrack' : 5000,
#     'Sonata' : 9000
# }
# print('Watch-Details : ',watch_details)
# print('Length : ',len(watch_details))
# print('Type : ',type(watch_details))
# print('Using Key ',watch_details['Titan'])
# print('-'*50)
# watch_details = {
#     'Titan' : 8000,
#     'Fasttrack' : 5000,
#     'Sonata' : 9000,
#     'Cartier' : 5000
# }
# print('Watch-Details : ',watch_details)
# print('Length : ',len(watch_details))
# print('Type : ',type(watch_details))
# print('Using Key ',watch_details['Titan'])
# watch_details['Cartier'] = 7988
# print('Watch-Details : ',watch_details)
# watch_details['Rolex'] = 657890849
# print('Watch-Details : ',watch_details)



# #Create

# snacks = {
#     'Vada' : 10,
#     'Samosa' : 12,
#     'Bajji' : 10,
#     'vadapav' : 50
# }
# print("Menu",snacks)
# snacks['vadapav'] = 45
# print("Menu after editing",snacks)
# snacks['panipoori']=40
# print("Menu after adding",snacks)


#Nested_Dictionary

users = {
    'raghul' : {
        'firstname' : 'raghul',
        'lastname'  : 'kumar',
        'location'  : 'madurai'
    },
    'ashok' : {
        'firstname' : 'ashok',
        'lastname'  : 'kumar',
        'location'  : 'madurai'
    },
    'guna' : {
        'firstname' : 'guna',
        'lastname'  : 'sekaran',
        'location'  : 'madurai'
    }
}

for i in users:
    print(users[i])
for i in users:
    print(users[i]['firstname'])
# for i in range(len(users)):
#     print(users[i])   
