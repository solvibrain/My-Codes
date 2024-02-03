import random

def swg(comp,mine):
    if(comp==mine):
        return None
    if(comp=="s"and mine=="g"):
        return True
    if(comp=="g" and mine=="w"):
        return True 
    if(comp=="w" and mine=="s"):
        return True
    else:
        return False

choice =('s','w','g')
comp= random.randint(0,2)
comp = choice[comp]
mine=input('choose either s,w or g :')

win = swg(comp,mine)
print(f"you chopse {mine} and computer choose {comp}")
if win is None:
    print("Match drawn")
if win is True:
    print("you won")
if win is False:
    print("you lose")        