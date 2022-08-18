import time

AGAIN_LIST = ["yes", "Yes", "no", "No"]

CHOICES = ["add","subtract","multiply","divide","+","-","*",":"]


def adder(number1, number2):
    result = number1 + number2
    return result

def substractor(number1, number2):
    result = number1 - number2
    return result

def multiplier(number1, number2):
    result = number1 * number2
    return result

def divider(number1,number2):
    result = number1 / number2
    return result


while True:
    print("--Calculator--")

    while True:
        try:
            number1 = int(input("enter the first number: "))       
        except ValueError:
            print("your input is not a number")
            continue
        else:
            break

    while True:
        try:
            number2 = int(input("enter the second number: "))       
        except ValueError:
            print("your input is not a number")
            continue
        else:
            break

    choice = ""
    while choice not in CHOICES:
        choice = input("What do you want to do? (add/subtract/multiply/divide) : ")
        if choice == "add" or choice =="+":
            print(adder(number1,number2))
        elif choice =="substract" or choice =="-":
            print(substractor(number1,number2))
        elif choice =="multiply" or choice =="*":
            print(multiplier(number1, number2))
        elif choice =="divide" or choice == ":":
            print(divider(number1,number2))

    again=""
    while again not in AGAIN_LIST:
        again = input("Calculate again? (Yes/No) : ")
    if again != "yes" and again != "Yes":
        break
         
print("Bye!")
time.sleep(1)


  
