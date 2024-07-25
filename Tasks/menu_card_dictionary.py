menu_operations = {
    'display': lambda menu_list: print('Menu Card : ', menu_list),
    'add': lambda menu_list, dish: menu_list.append(dish),
    'update': lambda menu_list, old_dish, new_dish: menu_list.__setitem__(menu_list.index(old_dish), new_dish) if old_dish in menu_list else print(f'{old_dish} not found in the menu'),
    'remove': lambda menu_list, dish: menu_list.remove(dish) if dish in menu_list else print(f'{dish} not found in the menu'),
    'veg_starter': ['paneer 65', 'chilly paneer', 'Veg Crispy'],
    'main': lambda: main()
}

def main():
    option = int(input('Enter the option \n To Display the Menu Card press -> 1 \n To Add the Starter in Menu Card press -> 2 \n To update the dish in Menu Card press -> 3  \n To remove the dish in menu card press -> 4 ' ))
    if option == 1:
        menu_operations['display'](menu_operations['veg_starter'])
    elif option == 2:
        add_starter = input('Enter the dish that want to be added : ')
        menu_operations['add'](menu_operations['veg_starter'], add_starter)
        print(f'{add_starter} added successfully')
        menu_operations['display'](menu_operations['veg_starter'])
    elif option == 3:
        menu_operations['display'](menu_operations['veg_starter'])
        update_starter = input('Enter the dish that want to be updated : ')
        new_dish_starter = input('Enter the New dish  : ')
        menu_operations['update'](menu_operations['veg_starter'], update_starter, new_dish_starter)
        print(f'{new_dish_starter} updated successfully')
        menu_operations['display'](menu_operations['veg_starter'])
    elif option == 4:
        menu_operations['display'](menu_operations['veg_starter'])
        remove_starter = input('Enter the dish that want to be removed : ')
        menu_operations['remove'](menu_operations['veg_starter'], remove_starter)
        print(f'{remove_starter} removed successfully')
        menu_operations['display'](menu_operations['veg_starter'])
    else:
        print("Enter the Correct Option")
        menu_operations['main']()

if __name__ == '__main__':
    menu_operations['main']()
