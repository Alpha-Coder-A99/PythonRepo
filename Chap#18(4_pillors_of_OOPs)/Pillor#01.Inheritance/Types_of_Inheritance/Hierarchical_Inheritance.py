#Multiple child classes inherit from the same single parent class
class Vehicle:
    def general_use(self):
        return "Transportation"

class Car(Vehicle):
    pass

class Bike(Vehicle):
    pass

