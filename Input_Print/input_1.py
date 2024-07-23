print('Enter your Name : ')
Name = input()
print('Myself',Name)

print()
Age = input('Age : ')
print('Your Age is : ',Age)
print('Type : ',type(Age))
birth_year = 2024 - int(Age)
print('Type : ',type(birth_year))
value_01 = int(input('Enter mobile number : '))
print("Entered number is : ",value_01)
print("Entered number is : ",type(value_01))


"""num1 = int (input('Enter the number 1'))
num2 = int (input('Enter the number 2'))
print("Original Number Entered are :",num1,num2)

temp = num1 
num1 = num2
num2 = temp

print('Swapped numbers are:',num1,num2)"""


"""num1 = int (input('Enter the number 1'))
num2 = int (input('Enter the number 2'))
print("Original Number Entered are :",num1,num2)

num1 = num1+num2
num2 = num1-num2
num1 = num1-num2

print('Swapped numbers using + and -:',num1,num2)"""

num1 = int (input('Enter the number 1'))
num2 = int (input('Enter the number 2'))
print("Original Number Entered are :",num1,num2)

num1 = num1*num2
num2 = num1/num2
num1 = num1/num2

print('Swapped numbers Using * and /:',num1,num2)