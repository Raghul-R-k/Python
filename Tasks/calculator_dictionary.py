arithmetic_operations = {
    'add': lambda num1, num2: print('Addition of two numbers : ', num1 + num2),
    'sub': lambda num1, num2: print('Subtraction of two numbers : ', num1 - num2),
    'multiply': lambda num1, num2: print('Multiplication of two numbers : ', num1 * num2),
    'div': lambda num1, num2: print('Division of two numbers : ', num1 / num2)
}

def main():
    print('Choose operation : ')
    print('1. Addition\n2. Subtraction\n3. Multiplication\n4. Division')
    select = int(input('Select 1/2/3/4 \n'))
    
    if select == 1:
        num1 = int(input('Enter 1st number : '))
        num2 = int(input('Enter 2nd number : '))
        arithmetic_operations['add'](num1, num2)
    elif select == 2:
        num1 = int(input('Enter 1st number : '))
        num2 = int(input('Enter 2nd number : '))
        arithmetic_operations['sub'](num1, num2)
    elif select == 3:
        num1 = int(input('Enter 1st number : '))
        num2 = int(input('Enter 2nd number : '))
        arithmetic_operations['multiply'](num1, num2)
    elif select == 4:
        num1 = int(input('Enter 1st number : '))
        num2 = int(input('Enter 2nd number : '))
        arithmetic_operations['div'](num1, num2)
    else:
        print("Invalid selection. Please choose 1/2/3/4.")
        main()
if __name__ == '__main__':
    main()
