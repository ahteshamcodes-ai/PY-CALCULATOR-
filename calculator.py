"""Python calculator"""

def add(a,b):
    return a + b
def subtract(a , b):
    return a - b
def multiply (a ,b):
    return a * b
def divide(a , b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero!")
    return a / b
def power (a ,b):
    return a ** b

def calculator():
    while True:
        print("\n======CALCULATOR======")
        print("1. Addition(+) ")
        print("2. Subtraction(-) ")
        print("3. Multiply(*) ")
        print("4. Divide(/) ")
        print("5. Power(**) ")
        print("6. Exit ")


        choice = input("Enter your choice(1-6): ").strip()

        if choice == "6":
            print("Thankyou for using the Calculator !!")
            break
        if choice not in ("1","2","3","4","5"):
            print("Invalid choice! please select (1-6).")
            continue

        try:

            num1 = float(input("Enter the number1: "))
            num2 = float(input("Enter the number2: "))

            if choice == "1":
                result = add(num1,num2)
            elif choice == "2":
                result = subtract(num1,num2)
            elif choice == "3":
                result = multiply(num1,num2)
            elif choice == "4":
                result = divide(num1,num2)
            elif choice == "5":
                result = power(num1,num2)
            
            print("Result" , result)
        except ValueError:
            print("Error: Please enter valid numbers.")
        except ZeroDivisionError as e:
            print("Error:", e)

if __name__ == "__main__":
    calculator()