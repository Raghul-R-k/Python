def Addition(value_1,value_2):
    Ans = value_1 + value_2
    return Ans
def Subtraction(value_1,value_2):
    Ans = value_1 - value_2
    return Ans
def Multiplication(value_1,value_2):
    Ans = value_1 * value_2
    return Ans
def Division(value_1,value_2):
    Ans = value_1 / value_2
    return Ans

def main():
    print('Choose operation : ')
    print('1.Addition\n2.Subtration\n3.Multiplication\n4.Division')
    select = int(input('Select 1/2/3/4 \n'))
    num01 = int(input('Enter 1st num : '))
    num02 = int(input('Enter 2nd num : '))

    if(select == 1):
        Ans = Addition(num01,num02)
        print(f'Addition {num01} and {num02}:',Ans)
    elif(select == 2):
        Ans = Subtraction(num01,num02)
        print(f'Subtration {num01} and {num02}:',Ans)
    elif(select == 3):
        Ans = Multiplication(num01,num02)
        print(f'Mutiplication {num01} and {num02}:',Ans)
    elif(select == 4):
        Ans = Multiplication(num01,num02)
        print(f'Mutiplication {num01} and {num02}:',Ans)
    else:
        print('choose the correct option')
        main()
if __name__ == '__main__':
    main()