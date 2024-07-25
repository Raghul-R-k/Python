#Write a program which will check the number is greater or equal to 70 and less than or equal to 90
def check_number(num):
    if (num >= 70 and num<=90):
        return num
def main():
    size = int(input('Enter the size : '))
    lst = []
    print('Enter the values')
    for i in range(size):
        value = int(input())
        lst.append(value)
    print('User List : ',lst)
    filter_list = list(filter(check_number,lst))
    print(filter_list)
if __name__ == '__main__':
    main()



