def DigitCounter():

    id = int(input("Enter Transaction ID :"))

    if id < 0 :
        print("Invalid Transaction ID")
    elif id == 0:
        print("Total Count : 1")
    else:
        count = 0
        while id > 0:
            id = id // 10
            count = count + 1

        print("Total Digits :",count)

def main():
    DigitCounter()

if __name__ == "__main__":
    main()