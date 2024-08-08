class Student:

    @staticmethod
    def RollNumber(y):
        print('Inside Static Method  : ',y)

    # @staticmethod
    # def RollNumber():
    #     print('Inside Static Method')


#Static Method Call 
Student.RollNumber(101)

#Using Object
s1 = Student()
s1.RollNumber(100)