def DiffSumOdd():

    No = int(input("Enter The Number :"))

    No = abs(No)

    even_sum = 0
    odd_sum = 0

    while No > 0:
        digit = No % 10

        if digit % 2 == 0:
            even_sum = even_sum + digit
        else:
            odd_sum = odd_sum + digit

        No = No // 10

    difference = even_sum - odd_sum

    print("Difference value :",difference)

def main():
    DiffSumOdd()

if __name__ == "__main__":
    main()