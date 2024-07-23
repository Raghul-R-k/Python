def main():
    length = int(input('Enter  the size of the list : '))
    list = []
    print('Enter the elements : ')
    for i in range(length):
        value = int(input())
        list.append(value)
    print('List : ',list)
    print('Maximum of the List : ',max(list))
def max(list):
    max = 0
    for i in list:
        if max < i:
            max = i
    return max
if __name__ == '__main__':
    main()
