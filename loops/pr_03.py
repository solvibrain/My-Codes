num=int(input("Enter the number : "))
prime=True
for i in range(2,int(num/2)):
    if num%i==0:
        print(f"{num} is not the prime nuimber . ")
        prime=False
        break
if prime is True:
    print(f"{num} is prime number . ")