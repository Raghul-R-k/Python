
# ex: make_car('Ford' , 'outback' ,color = 'Blue' , tow_package = True)

# solve the example



def make_car(*args,**kwargs):
    for i in args:
        print(i)
    for key,value in kwargs.items():
        print(key,':',value)
def main(): 
    make_car('Ford' , 'outback' ,color = 'Blue' , tow_package = True)
if __name__=="__main__":
    main()
