class Bagfactory:
    def __init__(self,metarial,zips,pockets):
        self.metarial=metarial
        self.zips=zips
        self.pockets=pockets

    def details(self):
        print(self.metarial)
        print(self.zips)
        print(self.pockets)

class Rebok(Bagfactory):
    def __init__(self,meterial,zips,pockets,color):
        super().__init__(self,meterial,zips,pockets)
        self.color=color
    def details(self):
        print(self.color)
        return super().details()
    
B1=Bagfactory("leather",3,4)
Reb1=Rebok("Polystor",5,7)


class Car:
    def __init__(self,type):
        self.type=type

    @staticmethod
    def start():
        print("Car is Starting ...")

    @staticmethod
    def stop():
        print("Car is stoping...")

class ToyotaCar(Car):
    def __init__(self, name,type):
        super().__init__(type)
        self.name=name 
        super().start()
car1=ToyotaCar("pirus","Electric")
print(car1.type)