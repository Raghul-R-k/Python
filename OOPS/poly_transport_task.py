class Transport:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

    def Display(self):
        print(f'{self.brand} and {self.model}')

class Car(Transport):
    pass

class Boat(Transport):
    pass

class Bike(Transport):
    pass

obj_1 = Car("Toyato","Supra")
obj_1.Display()

obj_2 = Boat("Yamaha","R674")
obj_2.Display()

obj_3 = Bike("Yamaha","RX100")
obj_3.Display()

