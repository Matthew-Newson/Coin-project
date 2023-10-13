Name = input("Name: ")
file = open("Coin_count.txt", "+r")
texts = file.readlines()
data = -1
lines = 0
count = 0
for line, text in enumerate(texts):
    lines = len(texts)
    while data == -1:
        data = text.find(Name)
        count += 1
        if data != -1:
            print(count)
            print("Name located") 
        elif count == lines:
            print("ERROR")
        else:
            break
        
            