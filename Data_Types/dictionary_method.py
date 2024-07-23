watch_details = {
    'Titan' : 8000,
    'Titan' : 8400,
    'Fasttrack' : 5000,
    'Sonata' : 9000
}

#keys() -> returns a list containing the dictionary 
# key_method = watch_details.keys()
# print('Key Method : ',key_method)

# value_method = watch_details.values()
# print('Value Method : ',value_method)

# get_method -> returns the value of specified key
get_method = watch_details.get('Titan')
print('Get Method : ',get_method)


# items_method() 
item_method = watch_details.items()
print('Item MEthod : ',item_method)



#update Method
watch_details.update({'Sonata' : 5463})
print('Update Method : ',watch_details)


#pop Method
watch_details.pop('Titan')
print('Pop Method',watch_details)

