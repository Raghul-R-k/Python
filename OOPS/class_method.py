#Class Method  


#Converting a function into class method
class student:
    graduation='BE'
    def Graduate_In(cls):
        print('Graduation in:',cls.graduation)
student.Graduate=classmethod(student.Graduate_In)
student.Graduate()

print()

#Converting a function into class method using Decorator
class student:
    graduation='BE'
    @classmethod
    def Graduate_In(cls):
        print('Graduation in:',cls.graduation)
student.Graduate_In()
