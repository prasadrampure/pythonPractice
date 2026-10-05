def ReverseIncresing():

    No = int(input("Enter the number :"))

    if No < 0:
        print("Not Increasing")
    else:
        original = No
        reverse = 0

        while No > 0:
            digit = No % 10
            reverse = reverse * 10 + digit
            No = No // 10

        if reverse > original:
            print("Increasing after reverse")
        else:
            print("Not Increasing")

def main():
    ReverseIncresing()

if __name__ == "__main__":
    main()