class College:
    CollegeName = "SFJV"

    
    def __init__(self,A,B):
        self.StudentName = A
        self.RollNo = B

    def Display(self):
        print("College name :",College.CollegeName)
        print("Student name :",self.StudentName)
        print("Enter RollNo :",self.RollNo)

obj = College("Prasad", 101)
print("Student Details :")
obj.Display()

    

    
