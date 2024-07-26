#Write an application which will append your existing file

import os

def append(filename,text_content):
    if os.path.exists(filename):
       file = open(filename,'a')
       file.write(text_content)
       print('Appended Sucessfully')
    else:
       print(f'{filename} Not Found')
       main()
    

def main():
    filename = input("Enter the file name that you want to append : ")

    text_content = input(f'Write a Content to Append in {filename} file : ')

    append(filename,text_content)


if __name__ == '__main__':
    main()