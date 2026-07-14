def Chkvowel(Char):
    if (Char == "A" or Char == "a" or
    Char == "E" or Char == 'e' or
    Char == "I" or Char == "i" or
    Char == "O" or Char == "o"  or
    Char == "U"  or Char == "u"):

        return True
    else:
        return False
    
def main():
    Char = (input("Enter a string :"))
    Ret = Chkvowel(Char)
    if(Ret):
        print("Char is vowel")
    else:
        print("Char is Consonant")

if __name__ == "__main__":
    main()