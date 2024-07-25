menu_card = {
    'Espresso'    : 550,
    'Mocha'       : 450,
    'Capachino'   : 560,
    'Americano'   : 650,
}
def display(list):
    print('Menu Card : ',list)
def Add(list,dish,price):
    list[dish]=price
    print(f'{dish} added succesfully')
def Update(list,dish,price):
    list.update({dish : price})
    print(f'{dish} price updated succesfully')
def Remove(list,dish):
    list.pop(dish)
    print(f'{dish} removed succesfully')

def main():
    option = int(input('Enter the option \n To Display the Menu Card press -> 1 \n To Add the Starter in Menu Card press -> 2 \n To update the dish in Menu Card press -> 3  \n To remove the dish in menu card press -> 4 \n' ))
    if option == 1 :
        display(menu_card)
    elif option == 2 :
        dish = input("Enter the Name of the Coffee : ")
        price = int(input("Enter the Price of the Coffee : "))
        Add(menu_card,dish,price)
        display(menu_card)
    elif option == 3 :
        display(menu_card)
        dish = input("Enter the Name of the Coffee that you update the price : ")
        price = int(input("Enter the Price of the Coffee : "))
        Update(menu_card,dish,price)
        display(menu_card)
    elif option == 4:
        display(menu_card)
        dish = input("Enter the Name of the Coffee that you want to remove : ")
        Remove(menu_card,dish)
        display(menu_card)
    else :
        print('Enter the correct option')
        main()
if __name__ == '__main__':
    main()