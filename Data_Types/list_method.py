# menu_card = ['Chicken','Mutton','Fish']
# print('Available items in menu card')

# #append()-->Adds an element at the end of the list
# menu_card.append('Kofta')
# print('After adding append method : ',menu_card)


# #extend() --> Add the elements of a list (or iterable) to the end of list 
# menu_card.extend(['Dal Tadka','Biryani'])
# print('Using Extend Method : ',menu_card)
# # menu_card.extend('Chappati') --> It'll iterate to the element and adds individual character

# #insert() --> Adds an element at the specified position
# menu_card.insert(1,'pulao')
# print('Using Insert Method : ',menu_card)

# #remove() method --> Will removed specified value 
# menu_card.remove('Dal Tadka')
# print('Using remove Method : ',menu_card)

# #pop() method --> removes a element of specified position 
# menu_card.pop(2)
# print('Using Pop Method : ',menu_card)


menu_card = ['Chicken','Mutton','Fish']
#index_method
index_method = menu_card.index('Mutton')
print("index  Method: ",index_method)


#sort Method 
menu_card.sort()
print("Sort Method : ",menu_card)

