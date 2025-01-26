#create a calculator
def Calculator (num1, num2, operator):

    if operator == "/" and num2 != 0:
        print(num1/num2)
    elif operator == "*":
        print(num1*num2)
    elif operator == "+":
        print(num1+num2)
    elif operator == "-":
        print(num1-num2)
    else:
        print("Invalid calculation")

num1 = float(input("Enter a number: "))  #automatically gets converted to string
operator = input("Enter an operator: ")
num2 = float(input("Enter another number: "))
print(Calculator(num1, num2, operator))
