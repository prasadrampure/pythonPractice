def CalculateMarks():
    N = int(input("Enter N :"))

    marks = list(map(int, input("Enter Marks :").split()))

    if N <= 0:
        print("Invalid Input")
    else:
        total = 0

        for mark in marks:
            if mark < 0 or mark > 100:
                print("Invalid Input")
                break

            total = total + mark
        else:
            print("Total Marks :",total)

def main():
    CalculateMarks()

if __name__ == "__main__":
    main()