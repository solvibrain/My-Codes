import random

def swg(comp,mine):
    if(mine==comp):
        return None
    elif(mine=='s' and comp=='w'):
        return True
    elif(mine=='w' and comp =='g'):
        return True
    elif(mine =='g' and comp =='s'):
        return True
    else:
        return False                 

 
choice = ['s','w','g']
comp = random.randint(0,2)
comp = choice[comp]

mine = input("Choose s,w or g : ")
win = swg(comp,mine)
print(f"you choose {mine} and comp choose {comp}.")
if win is None:
    print("Match drawn ")
elif win:
    print("you won the game .")
else: 
    print("you lose")    
