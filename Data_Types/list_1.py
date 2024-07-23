#Creating a list

#with same datatype
# course = ['Python','Java','C++']
# rollno = [12,34,56,78]

# #With mixed data type
mixed_type = ['Raghul',34,34.0,'gbasdjgysef']
# print('Heterogeneous',mixed_type)
# print('Length',len(mixed_type))

# #positive Index
# print('Index of Raghul ',mixed_type[0])
# print('Index of 34 ',mixed_type[1])
# print('Index of 34.0 ',mixed_type[2])
# print('Index of gbasdjgysef ',mixed_type[3])

# #Negative Index
# print('Index of Raghul ',mixed_type[-4])
# print('Index of 34 ',mixed_type[-3])
# print('Index of 34.0 ',mixed_type[-2])
# print('Index of gbasdjgysef ',mixed_type[-1])


#mutable (can change ,add and delete)
#Slicing : [start_index : ending_index(excluded)]
print('Slicing : ',mixed_type[0:3])
print('Neagtive Index Slicing : ',mixed_type[-4:-2])
 
fruits = ['Mango','Banana','Grapes','Water Melon']
fruits[1] = 'kiwi'
print('Using Index Replacing banana with kiwi : ',fruits)

del fruits[1]
print('After deleting kiwi : ',fruits)

fruits[1:3] = ['dragon_fruits','apple']
print('After adding dragon_fruit and apple instead of  Grapes & Water Melon : ',fruits)

