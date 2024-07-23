def display(list):
    print('Menu Card : ',list)
def Add(list,dish):
    list.append(dish)
def Update(list,dish_1,dish_2):
    list.replace(dish_1,dish_2)
def Remove(list,dish):
    list.remove(dish)
veg_starter = ['paneer 65','chilly panner','Veg Crispy']

def main():
    option = int(input('Enter the option \n To Display the Menu Card press -> 1 \n To Add the Starter in Menu Card press -> 2 \n To update the dish in Menu Card press -> 3  \n To remove the dish in menu card press -> 4 ' ))
    if(option == 1):
        display(veg_starter)
    elif(option == 2):
        add_starter = input('Enter the dish that want to be added : ')
        Add(veg_starter,add_starter)
        print(f'{add_starter} added successfully')
        display(veg_starter)
    elif(option == 3):
        display(veg_starter)
        update_starter = input('Enter the dish that want to be updated : ')
        new_dish_starter = input('Enter the New dish  : ')
        Update(veg_starter,update_starter,new_dish_starter)
        print(f'{new_dish_starter} updated successfully')
        display(veg_starter)
    elif(option == 4):
        display(veg_starter)
        remove_starter = input('Enter the dish that want to be removed : ')
        Remove(veg_starter,remove_starter)
        print(f'{remove_starter} removed successfully')
        display(veg_starter)
    else :
        print("Enter the Correct Option") 
        main()

if __name__ == '__main__':
    main()