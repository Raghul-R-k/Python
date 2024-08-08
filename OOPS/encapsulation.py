# Public : These are accessible from outside the class

# class Employee:
#     def __init__(self,name,salary) -> None:
#         self.name = name
#         self.salary = salary

#     def DisplaySalaryInfo(self):
#         print(f'{self.name} holding salary of {self.salary}')

# e1 = Employee('Raghul',200000000000)
# print(e1.salary)
# e1.DisplaySalaryInfo()


#Protected : (_Single underscore witin the class and its subclass)
class Employee:
    def __init__(self,name,salary) -> None:
        self.name = name #public
        self._salary = salary #protected

    def DisplaySalaryInfo(self):
        print(f'{self.name} holding salary of {self.salary}')

e1 = Employee('Raghul',200000000000)
print(e1.name)
print(e1._salary)

class Emp(Employee):
    print(e1._salary)
## e1.DisplaySalaryInfo()


#Private : (__Double  underscore witin the class)
# class Employee:
#     def __init__(self,name,salary) -> None:
#         self.name = name #public
#         self.__salary = salary #protected

#     def DisplaySalaryInfo(self):
#         print(f'{self.name} holding salary of {self.__salary}')

# e1 = Employee('Raghul',200000000000)
# print(e1.name)
# e1.DisplaySalaryInfo()
