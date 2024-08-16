import time

YES_LIST = ["yes", "Yes", "y","Y"]
NO_LIST = ["no", "No","n","N"]

CHOICES = ["add","subtract","multiply","divide","+","-","*",":","/","exit"]


def adder(number1, number2):
    result = number1 + number2
    return result

def subtractor(number1, number2):
    result = number1 - number2
    return result

def multiplier(number1, number2):
    result = number1 * number2
    return result

def divider(number1,number2):
    result = number1 / number2
    return result


print("---Calculator---")


while True:

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
            print(subtractor(number1,number2))
        elif choice =="multiply" or choice =="*":
            print(multiplier(number1, number2))
        elif choice =="divide" or choice == ":" or choice == "/":
            print(divider(number1,number2))
        elif choice == "exit":
            exit()

    again=""
    while again not in YES_LIST and again not in NO_LIST:
        again = input("Calculate again? (Y/N) : ")
    if again in NO_LIST:
        break
      
print("Bye!")
exit()


  
