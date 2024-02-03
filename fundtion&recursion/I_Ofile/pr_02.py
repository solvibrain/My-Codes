import random
def game():
    score=random.randint(1,100)
    print(f"The Score is {score}")
    return score

score=game()

with open("Hiscore.txt","r") as f:
    Hiscore= int(f.read())

if (Hiscore<score):
    with open("Hiscore.txt","w") as f:
        f.write(str(score) )   

