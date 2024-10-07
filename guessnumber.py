import random

number = random.randrange(10)
guess = 0
chances = 3
for i in range(3):
    
    myguess = int(input("enter number:"))
    
    if(myguess == number):
        print("Your guess is correct")
        break
    elif(myguess > number):
        print("Your guess is higher")
    elif(myguess < number):
        print("Your guess is lesser")
    
if(myguess != number):
    print("GAME OVER!")
