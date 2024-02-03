n1=int(input("Enter the number : "))
n2=int(input("Enter the numbe2 : "))
n3=int(input("Enter the numbe3 : "))
n4=int(input("Enter the numbe4 : "))
if(n1>n2 and n1>n3 and n1>n4):
    print(n1,"is greatest number. ")
elif(n2>n1 and n2>n3 and n2>n4):
    print(n2,"is greatest number. ")
elif(n3>n2 and n3>n1 and n3>n4):
    print(n3,"is greatest number. ") 
else:
    print(n4, "is the greatest number . ")               