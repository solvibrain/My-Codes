import random

comp = random.randint(1,3)

guess = int(input("Guess the number : "))
attempt =1

while(True) :
    if(guess>comp):
        guess=int(input("guess lower number : "))
        attempt +=1
    elif(guess<comp):
        guess =int(input("Gues the higher number : "))
        attempt +=1

    else:
        print(f'you won the game in {attempt}.')        

        break