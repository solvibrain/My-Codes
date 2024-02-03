import string
import random
symbols=[]
symbols=list(string.ascii_letters)
card1=[0]*5
card2=[0]*5
pos1=random.randrange(0,5)
pos2=random.randrange(0,5)
print(pos1)
print(pos2)
# setting the position randomly using the random range function which is taking value from starting point and exclusive the last pointf
sameletter=random.choice(symbols)
symbols.remove(sameletter)

if (pos1==pos2):
    card1[pos1]=sameletter
    card2[pos1]=sameletter

else:
    card1[pos1]=sameletter
    card2[pos2]=sameletter
    card1[pos2]=random.choice(symbols)
    symbols.remove(card1[pos2])
    card2[pos1]=random.choice(symbols)
    symbols.remove(card2[pos1])

i=0
while(i<5):
    if(i!=pos1 and i!=pos2):
        alpha1=random.choice(symbols)
        card1[i]=alpha1
        symbols.remove(alpha1)
        alpha2=random.choice(symbols)
        card2[i]=alpha2
        symbols.remove(alpha2)
    i=i+1  

print(card1)      
print(card2)
ch=input("Enter the matched character in both the list : ")      
if(ch==sameletter):
    print("yout have choosed the right the letter from the list")
elif ((ch not in symbols) and (ch not in card1) and (ch not in card2)):
    print("Wrong Entry please input right choice:")
else:
    print("wrong choice better luck next time::Good bye.")