def StaffDetails(**kwargs):
    for key,value in kwargs :
        print(f'{key} is {value}')
def main():
    changepond = {
        'Name' : 'Raghul',
        'Age'  : 23,
        'Contact' : 6379616860,
        'Email'  : 'raghulsundhar2001@gmail.com'      
        }
    StaffDetails(**changepond)
if __name__ == '__main__':
    main()
    
