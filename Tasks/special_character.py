def special_characters():
    line = input('Enter any string : ')
    s_c = '[@_!#$%^&*()<>?/|\}{~:]'
    for i in line:
        if i in s_c:
            print('There is special characters')
            break
    else :
        print('There is no special characters')

if __name__ == '__main__':
    special_characters()