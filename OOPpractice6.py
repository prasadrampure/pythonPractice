class Animal:

    def Sound(self):
        print("Animal make sound")

class dog(Animal):

    def Sound(self):
        print("Barks")

class Cat(Animal):

    def Sound(self):
        print("Meowwwwwww")

dobj = dog()
cobj = Cat()

dobj.Sound()
cobj.Sound()
