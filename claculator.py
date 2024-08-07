
while True:
    num1 = int(input("Enter first number: "))
    opr = input("Enter the operator(+, -, *, /, %): ")
    num2 = int(input("Enter second number: "))
    if(opr=="+"):
        print(num1+num2)
    elif(opr=="-"):
        print(num1-num2)
    elif(opr=="*"):
        print(num1*num2)
    elif(opr=="/"):
        print(num1/num2)
    elif(opr=="%"):
        print(num1%num2)
    else:
        print("Invalid Operator")
    choice = input("Would you like to make another calculation (Yes/No): ")
    choice = str.lower(choice)
    if(choice=="yes" or choice=="y"):
        continue
    else:
        break;