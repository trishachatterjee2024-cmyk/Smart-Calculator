from operations import *

history = []

def save_to_file(result):
    with open("history.txt", "a") as file:
        file.write(str(result) + "\n")

while True:
    print("\n==== SMART CALCULATOR ====")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")
    print("6. Square Root")
    print("7. Show History")
    print("8. Exit")

    choice = input("Choose option: ")

    if choice == "8":
        print("Exiting...")
        break

    try:
        if choice in ["1","2","3","4","5"]:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == "1":
                result = add(num1, num2)
            elif choice == "2":
                result = subtract(num1, num2)
            elif choice == "3":
                result = multiply(num1, num2)
            elif choice == "4":
                result = divide(num1, num2)
            elif choice == "5":
                result = power(num1, num2)

            print("Result:", result)
            history.append(result)
            save_to_file(result)

        elif choice == "6":
            num = float(input("Enter number: "))
            result = square_root(num)
            print("Result:", result)
            history.append(result)
            save_to_file(result)

        elif choice == "7":
            print("History:", history)

        else:
            print("Invalid choice!")

    except:
        print("Invalid input!")