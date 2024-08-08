# class Arithmetic:
#     def __init__(self,value) -> None:
#         self._value = value  #protected attribute

#     def getValue(self):
#         print('To retrive the value of \'_value\'')
#         return self._value
    
#     def setValue(self,value):
#         print('Setting value to ' +value)   #new value/updated
#         self._value = value

#     def delValue(self):
#         print('Deleting the value')
#         del self._value

#     value = property(getValue,setValue,delValue)

# A1 = Arithmetic(12)
# print(A1.value)

# A1.value = "Raghul"
# del A1.value


#Using Decorator

class Arithmetic:
    def __init__(self, value) -> None:
        self._value = value  # Protected attribute

    @property
    def value(self):
        print('To retrieve the value of \'_value\'')
        return self._value
    
    @value.setter
    def value(self, value):
        print('Setting value to ' + value)  # New value/updated
        self._value = value

    @value.deleter
    def value(self):
        print('Deleting the value')
        del self._value

A1 = Arithmetic(12)
print(A1.value)  

A1.value = "Raghul"  
print(A1.value)  

del A1.value   

