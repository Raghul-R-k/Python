def main():
    size = int(input('Enter the size : '))
    lst = []
    print('Enter the values')
    for i in range(size):
        value = int(input())
        lst.append(value)
    print('User List : ',lst)
    filter_list = list(filter(lambda num : num >= 70 and num<=90,lst))
    print(filter_list)
if __name__ == '__main__':
    main()