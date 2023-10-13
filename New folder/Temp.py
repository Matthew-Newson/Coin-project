import os
Name = input("Name: ")
file = open("Coin_count.txt", "+r")
texts = file.readlines()
for lines, text in enumerate(texts):
    data = text.find(Name)
    print(data)