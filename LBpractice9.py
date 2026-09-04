def CheckVoterID():

    Num = int(input("Enter Voter ID :"))

    if Num < 0:
        print("Rejected")
    else:
        count = 0

        while Num > 0:
            Num = Num // 10
            count = count + 1

        if count > 5:
            print("Accepted")
        else:
            print("Rejected")
            
def main():
    CheckVoterID()
 
if __name__ == "__main__":
    main()