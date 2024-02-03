# import imp


import pickle

# l=[32,534,646]
# file=open("data.txt","wb")
# pickle.dump(l,file)
# file.close()
file=open("data.txt","rb")
d=pickle.load(file)
print(d)
