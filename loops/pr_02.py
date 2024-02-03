l1=[]
for i in range(1,10):
    l1[i]=input("Enter the name of the participants  : ")

for name in l1:
    if name.startswith('s'):
        print(f"Hello ,{name}\n \t you name is being selected form the 100000 people in our list.")
