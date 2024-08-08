#Class Method  


#Converting a function into class method
class student:
    graduation='BE'
    name = 'Raghul'


    def name__(self):
        self.name = "manoj"
        print(self.__class__.name)    
        print(self.name)


    def Graduate_In(cls):
        print('Graduation in:',cls.graduation)


obj1 = student()
obj1.name__()  

student.Graduate = classmethod(student.Graduate_In)
student.Graduate()


# print()

#Converting a function into class method using Decorator


class student:
    graduation='BE'
    @classmethod
    def Graduate_In(cls):
        print('Graduation in:',cls.graduation)
student.Graduate_In()
