with open("poem.txt","r") as f:
    if("Twinkle" in f.read()):
        print("yes twinkle is present in the file.")
    else:
        print("NO Twinklw is not presentin the file.")    