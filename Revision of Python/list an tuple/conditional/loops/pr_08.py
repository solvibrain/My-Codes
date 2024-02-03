from argparse import RawDescriptionHelpFormatter


n=int(input("Enter the number : "))

for i in range(1,n+1):
    for j in range(i):
        print("*",end="")
    for j in range(3-i):
        print(" ",end="")
    print("\n",end="")        