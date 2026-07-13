def Area(Radius):
    return 3.14 * Radius * Radius

def Circumference(Radius):
    return 2 * 3.14 * Radius

def main():
    Radius = int(input("Enter a radius :"))

    Ret = Area(Radius)
    print("Area is :",Ret)
    Ret = Circumference(Radius)
    print("Circumference is :",Ret)

if __name__ == "__main__":
    main()