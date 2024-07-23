# #Create a tuple 
# #Homegeneous
# student_id = (123,233,433,232)
# ice_cream = ('Vanilla','Choco-chips','Blueberry')

# #Heterogeneous
# mixed_type  =  (123,'Hello',False,45.54)

#len() 
#using index ==> BlackCurrent(positive) 
#using index ==> False(Negative index) 
#using slicing ==> 'Hello', False  

# print(len(student_id))
# print(ice_cream[2])
# print(mixed_type[-2])
# print(mixed_type[1:3])


# ice_cream = ('Vanilla',)
# print(type(ice_cream))


#immutable (cannot modify,delete or Add)
# mixed_type[0] = True
# print("False ",mixed_type)

ice_cream = ('Vannila','Choco-chips','Blueberry','Vannila')
count_method = ice_cream.count('Vannila')
print('Count Method : ',count_method)

index_method = ice_cream.index('Vannila')
print('Index Method : ',index_method)
