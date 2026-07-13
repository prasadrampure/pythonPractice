def Area(lenght,breadth):
    return lenght * breadth

def Perimeter(lenght,breadth):
    return 2 * (lenght + breadth)

def main():
    length = int(input("Enter a lenght :"))
    breadth = int(input("Enter a breadth :"))

    Ret = Area(length,breadth)
    print("Area is :",Ret)

    Ret = Perimeter(length,breadth)
    print("Perimeter is :",Ret)

if __name__ == "__main__":
    main()