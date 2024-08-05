import datetime

today = datetime.date.today()
year = today.year
print(year)

try : 
    # num1 = int(input('Enter the Number 1 : '))
    # num2 = int(input('Enter the Number 2 : '))

    # result = num1/num2
    # print(result)

    items = ['Bread','Butter','Jam','Cheese']
    # items[len(items)] = "Spread"
    num1 = int(input('Enter the Number 1 : '))
    assert num1 % 2 == 0
    print(items)


except ZeroDivisionError:
    print('Error : Denominator cannot be Zero')

except ValueError:
    print('Only NUmbers are allowed')

except IndexError:
    print('Kindly use insert or append method')

except AssertionError:
    print('Entered value is not matching the test condition')

else :
    print(num1 , 'is Even ')


finally:    #Finally runs irrespective of error
    print('Program is over')

year_of_birth = int(input('Enter the year of birth : '))

age = year - year_of_birth

if(age < 18):
    raise Exception(f'The age should be greater than 18 and your age is {age}')

print(age)
