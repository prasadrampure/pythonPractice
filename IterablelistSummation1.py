def main():
    Numbers = [10, 20, 30, 40, 50]

    for num in Numbers:
        print(num)

    Numbers[0] = 60
    Numbers[1] = 70
    Numbers[2] = 80
    Numbers[3] = 90
    Numbers[4] = 100

    print("-"*20)

    for num in Numbers:
        print(num)

if __name__ == "__main__":
    main()
