def greatest(num1,num2,num3):
    if(num1>num2):
        b=num1
    else:
        b=num2
    if(num3>b):
        b=num3


    return     b    

a=int(input("Enter the num1 :  "))
b=int(input("Enter the num2 :  "))
c=int(input("Enter the num3 :  "))
a=greatest(a,b,c)
print(a)    