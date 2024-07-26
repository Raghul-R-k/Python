#Write an application which will duplicate files
import os 
import filecmp

def duplicate(filename_1,filename_2):
    if filecmp.cmp(filename_1,filename_2) :
        os.remove(filename_1)
        print(f'{filename_2} duplicate file deleted')
    else :
        print(f'{filename_1} and {filename_2} are different ')


def main():
    filename_1 = input('Enter the 1st filename : ')
    if(os.path.exists(filename_1)):
        filename_2 = input('Enter the 2nd filename : ')
        if(os.path.exists(filename_2)):
            duplicate(filename_1,filename_2)
        else :
            print('Enter the correct second filename!!!!!')
    else :
        print('Enter the correct first filename!!!!!!!!')

if __name__ == '__main__':
    main()