def main():
    length = int(input('Enter  the size of the list : '))
    list = []
    print('Enter the elements : ')
    for i in range(length):
        value = int(input())
        list.append(value)
    print('List : ',list)
    print('Sum of the List : ',sum(list))

def sum(list):
    total = 0
    for i in list:
        total += i
    return total
if __name__ == '__main__':
    main()

