num = int(input("Enter the number : "))

for i in range(1,num+1):
    for j in range(num-i):
        print(" ",end="")
    for j in range(2*i-1):
        print("*",end="")
    for j in range(num-i):
        print(" ",end="")
    print("\n",end="") 
