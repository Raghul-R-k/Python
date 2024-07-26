import os

def create_file(file_name):
    if os.path.exists(file_name):
        print("You already have this file")
        main()
    else :
        print("Your file have been created")
        return open(file_name,"w")
def write_file(filename01,filename02):
    if os.path.exists(filename02):
        exit_data = open(filename02,"r")
        data_file = exit_data.read()
        filename01.write(data_file)
        print(f'Your {filename01} File have been created and copied successfully')
    else :
        print('Enter the correct file name in the folder ')
        main()
def main():
    file_name = input("Enter the New file name :")
    file_1 = create_file(file_name)
    copy_file = input("Enter the file name that you want to copy from :")
    write_file(file_1,copy_file)
 
if __name__ == "__main__":
    main()