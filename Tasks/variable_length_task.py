def make_sandwich(sandwich, *toppings):
    toppings_str = ''
    for i in toppings:
        toppings_str = i + ',' + toppings_str
    print(f'Your {sandwich} with {toppings_str} is ready.')

def main():
    sandwiches = ['Chicken Sandwich', 'Egg Sandwich', 'Roast Chicken Sandwich', 'Grilled Chicken Sandwich']
    toppings = ['lettuce', 'tomato', 'corn', 'cheese', 'mayo']

    print('Please choose a type of sandwich:')
    for index, sandwich in enumerate(sandwiches,1):
        print(f'{index}. {sandwich}')
    
    sandwich_choice = int(input('Enter the number of your choice: '))

    if(sandwich_choice < 1 or sandwich_choice > 4):
        print('Invalid choice. Please try again.')
        print()
        main()
    
    chosen_sandwich = sandwiches[sandwich_choice - 1]

    print('\nPlease choose your toppings (separated by comma, e.g., 1,3,5):')
    for index, topping in enumerate(toppings,1):
        print(f'{index}. {topping}')
    
    topping_choices = input('Enter the numbers of your choices: ').split(',')
    chosen_toppings = []

    for i in topping_choices:
        index = int(i)
        if index >= 1 and index <= 5:
            chosen_toppings.append(toppings[index - 1])
        else:
            print(f'Invalid topping choice: {i}')
            main()
    
    make_sandwich(chosen_sandwich, *chosen_toppings)

if __name__ == '__main__':
    main()
