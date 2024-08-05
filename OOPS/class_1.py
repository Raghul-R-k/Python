#Creating class 

class Student:
    def __init__(self,firstname,lastname):
        self.firstname = firstname #instance variable #properties
        self.lastname = lastname

    def Display(self):  #instance method
        print(f'{self.firstname} {self.lastname}')


Obj1 = Student('Raghul','Kumar')
# print(Obj1.firstname)
Obj1.Display()