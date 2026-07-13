def Fahrenheit(Celsius):
    return (Celsius * 9/5)+32

def main():
    Celsius = int(input("Enter a temperature :"))

    Ret = Fahrenheit(Celsius)
    print("Fahrenheit is :",Ret)


if __name__ == "__main__":
    main()