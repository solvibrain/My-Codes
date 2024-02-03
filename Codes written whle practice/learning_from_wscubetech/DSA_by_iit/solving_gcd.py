# first and simple way to solve the problem of gcd

def gcd(m,n):
    fm=[]
    for i in range(1,m+1):
        if m%i==0:
            fm.append(i)
    cf=[]
    for f in fm:
        if n%f==0:
            cf.append(f)        
    return cf[-1]        

a=int(input("Enter the num1 : "))
b=int(input("Enter the num2 : "))
print("Gcd of the given two number is ",gcd(a,b) )


# Second way  to solve the problem of finding gcd

def gcd(m,n):
    cf=[]
    for i in range(1,min(m,n)+1):
        if m%i==0 and n%i==0:
            cf.append(i)
    return cf[-1]        

print("Gcd of the given two number is ",gcd(a,b) )


# The best and Simplified way to solve the problem is using Euclids algorithm

def gcd(m,n):
    if n>m: # checking the condition that 
        # (m,n)=(n,m)# swaping the values if conditions satisfies.this type of swapping is only valid in pyhon in other programming language this is being done by using temp varaibel
        temp=m # this is other way of swapping that other programming language also hold.
        m=n
        n=temp
    if m%n==0:#if m divides n then gcd will be n 
        return n
    else:
        return(gcd(max(n,m-n),min(n,m-n)))# if all conditions does not satisfies this is condition of recursion 

# Above same function can also be formulated using the while loop


    
print("Gcd of the given two number is ",gcd(a,b) )#this is for printing the value that is being return by the function 

def gcd(m,n):
    if n>m:
        (m,n)=(n,m)
    while(m%n)!=0:
        (m,n)=(max(n,m-n),min(n,m-n) )          
    return (n)

print("Gcd of the given two number is ",gcd(a,b) )#this is for printing the value that is being return by the function 
