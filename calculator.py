def calculator():
    number1=int(input("Enter a number:"))
    number2=int(input("enter a second number:"))
    operation=input("+(addition) or - (substraction) or *(multiplication) or / (division):")
    if operation=="+":
        number=number1+number2
        print(f"{number1}+{number2}={number}")
    elif operation  == "-":
        number = number1 - number2
        print(f"{number1} - {number2} = {number}")
    elif operation == "*":
        number = number1 * number2
        print(f"{number1}*{number2}={number}")
    elif operation == "/":
        number = number1 / number2
        print(f"{number1}/{number2}={number}")
    else:
        print("invalid choose! ")
calculator()