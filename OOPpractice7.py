class Vehical:

    def Start(self):
        print("Engine is start")

class Car(Vehical):

    def Start(self):
        print("Car is start")

class Bike(Vehical):

    def Start(self):
        print("Bike is start")

cobj = Car()
bobj = Bike()

cobj.Start()
bobj.Start()

