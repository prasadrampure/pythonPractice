class Rectangle:

    def __init__(self,A,B):
        self.Lenght = A
        self.Width = B

    def Area(self):
        Area = (self.Lenght * self.Width)

        print("Area is :",Area)

    def Perimeter(self):
        Perimeter = 2 * (self.Lenght + self.Width)

        print("Perimeter is :",Perimeter)

No1 = int(input("Enter the lenght"))
No2 = int(input("Enter the Width"))

obj = Rectangle(No1,No2)
obj.Area()
obj.Perimeter()
