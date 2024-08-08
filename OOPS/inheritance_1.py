class Person:
    def __init__(self,identify,name):
        self.identify=identify
        self.name=name
    def Display(self):
        print(f"Name:{self.name} Id:{self.identify}")
 
class Employee(Person):
    def __init__(self,identify,name,salary):
        self.salary = salary
        #person.__init__(self,identify,name)
        super().__init__(identify,name)
    def Display(self):
        super().Display()
        print(f"Salary: {self.salary}")
# e1 = Person("Raghul",123)
# e1.Display()
e1=Employee('Raghul',123,15000)
e1.Display()
print(e1.salary)

#parent class/base class
class Person:
    def __init__(self,identity,name):
        self.identity=identity
        self.name=name

    def displayInfo(self):
        print(f'Name: {self.name} Id:{self.identity}')

class Employee(Person):  #derived class
    def __init__(self, identity, name,salary):
        super().__init__(identity, name)
        self.salary=salary
    def show(self):
        print("Inside Child")

e1=Employee(4443,"Raghul",25000)
e1.displayInfo()
e1.show()
print(e1.salary)