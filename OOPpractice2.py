class Employ:
    
    def __init__(self,Name,Salary):
        self.Name = Name
        self.Salary = Salary

    def Display(self):
        print("Name :",self.Name)
        print("Salary :",self.Salary)

obj = Employ("Prasad", 10000)
obj.Display()
        