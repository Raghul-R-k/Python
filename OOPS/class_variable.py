#Creating Class
class Student:
    graduation = 'BE'  #Class Variable
    def __init__(self,firstname,lastname):
        self.firstname = firstname
        self.lastname = lastname
   

Obj1 = Student('Raghul','Kumar')
# print(Obj1.graduation)
print(Obj1.__class__.graduation)



#Creating Class

class Student:
    Graduation = "BE"
    def __init__(self,firstname,lastname):
        self.firstname = firstname      #instance variable  #Properties
        self.lastname = lastname
        self.Graduation = "ME"

    def Display(self):
        print(f'{self.firstname} {self.lastname}')

obj = Student("Raghul","Kumar")
Student.Display(obj)

print(obj.Graduation)
print(obj.__class__.Graduation)