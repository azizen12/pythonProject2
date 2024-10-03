def function_one():
    print("Function One is running!")

def function_two():
    print("Function Two is running!")

def function_three():
    print("Function Three is running!")

def function_four():
    print("Function Four is running!")

def main():
    print("Select a function to run:")
    print("1: Function One")
    print("2: Function Two")
    print("3: Function Three")
    print("4: Function Four")

    choice = input("Enter the number of the function you want to run (1-4): ")

    if choice == '1':
        function_one()
    elif choice == '2':
        function_two()
    elif choice == '3':
        function_three()
    elif choice == '4':
        function_four()
    else:
        print("Invalid choice. Please select a number between 1 and 4.")

if __name__ == "__main__":
    main()
