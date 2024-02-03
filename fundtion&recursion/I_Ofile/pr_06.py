with open('file.txt','r') as f:
    text = f.read()
word = input("Enter the word : ")

if( word in text):
    print('yes it in the file.')
else :
    print("No this is not present in the file . ")    