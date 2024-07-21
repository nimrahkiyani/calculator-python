import math


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y

def power(x , y):
    return x**y

def root(x):
    return math.sqrt(x)

def cos(x):
    return math.cos(x)

def sin(x):
    return math.sin(x)

def tan(x):
    return math.tan(x)


print("******Calculator using Python******")
print("--------------------------------------")

print("\t\tSelect operation")
print("1.Add     2.Subtract  3.Multiply")
print("4.Divide  5.Power     6.Root")
print("7.Cos     8.Sin       9.tan")

while True:
    # take input from the user
    choice = input("Enter choice: ")

    # check if choice is one of the four options
    if choice in ('1', '2', '3', '4' , '5'):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))

        elif choice == '5':
            print(num1, "^", num2, "=", power(num1, num2))


        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
            break
    elif choice in ('6' , '7' , '8' , '9'):
        try:
            num1 = float(input("Enter number: "))

        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == '6':
            print("square root of ", num1, "=", root(num1))

        elif choice == '7':
            print("Result : " , cos(num1))

        elif choice == '8':
            print("Result : " , sin(num1))

        elif choice == '9':
            print("Result : " , tan(num1))


        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
            break

    else:
        print("Invalid Input")