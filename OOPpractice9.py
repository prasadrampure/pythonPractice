class person:

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def Display(self):
        print("Person Name :",self.name)
        print("Person Age :",self.age)

class Employe(person):
    def __init__(self,name,age,Id,Salary):
        super().__init__(name,age)
        self.Id = Id
        self.Salary = Salary

    def Display(self):
        super().Display()
        print("Employe Id is :",self.Id)
        print("Employe Salary is :",self.Salary)

obj = Employe("Prasad" , 20 , 1234 , 10000)
obj.Display()
