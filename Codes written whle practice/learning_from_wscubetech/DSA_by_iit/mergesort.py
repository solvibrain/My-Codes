 # Here programme is being written for merging two sorted list

from cmath import log


def merg(a,b):
    (c,m,n)=([],len(a),len(b))
    (i,j)=(0,0)
    while i+j<m+n:
        if i==m:
            c.append(b[j])
            j=j+1
        elif j==n:
            c.append(a[i])    
            i=i+1
        elif a[i]<b[j]  :
            c.append(a[i])  
            i=i+1
        elif b[j]<a[i]:
            c.append(b[j])    
            j=j+1
    return (c)

a=list(range(1,100,2))           
b=list(range(0,100,2))
print(a,b)
print(merg(a,b))




# a=list(range(1,100,2))
# print(a)