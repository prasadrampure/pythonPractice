def AutoSettelment():

    No = int(input("Enter Transaction Number :"))

    if No > 0 and No % 10 == 0:
        return "Auto Settelment Allowed"
    else:
        return "Not Allowed"
    
def main():
    Ret = AutoSettelment()
    print(Ret)

if __name__ == "__main__":
    main()