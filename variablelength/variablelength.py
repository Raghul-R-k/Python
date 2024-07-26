# def sum_all(*args):
#     count = 0
#     for i in args:
#         count += i
#     return count

# output = sum_all(1,2,3,4,5)
# print('Sum : ',output)



def name (*args,**kwargs):
    # for name in args:
    #         print(name)
    print(kwargs)
    print(args)
       
def  main():
    print(1)
    fresher = ['Ajith','Gokul','Vijay','Prasanth']
    s={'name':"sa",'name2':3}
    name('Ajith','Gokul','Vijay','Prasanth',**s)


if __name__ == '__main__':
    main()
 
