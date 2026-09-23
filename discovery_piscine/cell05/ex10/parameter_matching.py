import sys
def main():
    if len(sys.argv) != 2:
        print("none")
        return

    user_input = input("What was the parameter? ")
    
    if user_input == sys.argv[1]:
        print("Good job!")
    else:
        print("Nope, sorry...")

if __name__ == "__main__":
    main()