from functools import reduce
def main():
    size = int(input('Enter the Size : '))
    lst = []
    print('Enter Values : ')
    for i in range(size):
        value = int(input())
        lst.append(value)
    print('User List : ',lst)
    map_list = list(map(lambda num : num ** 3,lst))
    print('Map List : ',map_list)
    print()
    reduce_list = reduce((lambda num1,num2 : num1+num2),map_list)
    print('Reduce LIst : ',reduce_list)
if __name__ == '__main__':
    main()    