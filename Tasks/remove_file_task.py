import os

def remove(filename) :
    if os.path.exists(filename):
        os.remove(filename)
        print('Your file have been Deleted ')
    else :
        print('Enter the correct file name ')
        main()
def main():
    remove_file = input("Enter the file that want to be removed : ")
    remove(remove_file)
if __name__ == '__main__':
    main()