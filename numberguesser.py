import random

print("---Number Guesser---")

YES_LIST = ["yes", "Yes", "y","Y"]
NO_LIST = ["no", "No","n","N"]

while True:

    Number = random.randint(0,1000)
    Tries = 1

    #print(Number)   

    while True:
        
        while True:
            try:
                guess = int(input("enter your guess: "))     
            except ValueError:
                print("your input is not an integer!")
                continue
            else:
                break
    
        
        if Number == guess:
            print("Yes! The Number is " + str(Number))
            print("You tried " + str(Tries) + " times!")
            break
    
        if Number > guess:
            print("The Number is bigger!")
            Tries +=1

        if Number < guess:
            print("The Number is smaller!")
            Tries +=1

    again=""
    while again not in YES_LIST and again not in NO_LIST:
        again = input("Calculate again? (Y/N) : ")
    if again in NO_LIST:
        break

    