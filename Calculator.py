def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def  multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

print("Select Operation: ")
print("+ Add")
print("- Subtract")
print("* Multiply")
print("/ Divide")

operator = input("Enter the operator: ")

num1 = float(input("Enter the First Number: "))
num2 = float(input("Enter the Second Number: "))

if operator == '+':
    print(num1, "+" , num2, "=" , add(num1, num2))

elif operator == '-':
    print(num1, "-", num2, "=" , subtract(num1, num2))

elif operator == '*':
    print(num1, "*" , num2, "=" , multiply(num1, num2))

elif operator == '/':
    print(num1, "/" , num2, "=" , divide(num1, num2))

else:
    print("Invalid input")