#ALL IMPORTS
from time import sleep
import json
import sys

#DECLARING CONSTANTS
DATA = {
        "Name1" : " ",
        "Total_count": 0,
        "Accuracy" : 0,
        "Correct" : 0,
        }

COINTYPE = [0.01, 0.02, 0.05, 0.10, 0.20, 0.50, 1.00, 2.00] 
COIN_DICTIONARY = {      #Dictionary that uses coin input as a key to get coin weight and bag weight
    "Coin Weight" : {
        0.01 : 3.56,
        0.02 : 7.12,
        0.05 : 2.35,
        0.10 : 6.50,
        0.20 : 5.00,
        0.50 : 8.00,
        1.00 : 8.75,
        2.00 : 12.00
    },
    "Bag weight" : {
        0.01 : 356.00,
        0.02 : 356.00,
        0.05 : 235.00,
        0.10 : 325.00,
        0.20 : 250.00,
        0.50 : 160.00,
        1.00 : 175.00,
        2.00 : 120.00

    },
}

#DEFINING FUNCTIONS
def Calculator(Weight,Real_Coin,Bag_weight,correct):  #Calculates how many coins you need to add and remove from your bag
    if Weight > Bag_weight:
        difference = Weight - Bag_weight
        difference2 = difference / Real_Coin
        print ("You need to Remove " +str (difference2) , " coins from bag")
        sleep(1)
    if Weight < Bag_weight:
        difference = Bag_weight - Weight
        difference2 = difference % Bag_weight
        difference3 = difference2 / Real_Coin
        print ("You need to add " +str (difference3) , " coins from bag")
        sleep(1)
    if Weight == Bag_weight:
        print("Bag weight is correct")
        sleep(1) 
        return True

def adduser(): #Updates file if name is already in file
    Name = input("What is your name? ")
    if Name in texts:
        ("Name already in use")
        sleep(1)
        menu()
    else:
        DATA.update({"Name1":Name})
        DATA.update({"Total_count": "0"})
        DATA.update({"Accuracy": "0"})
        with open("Coin_count.json", "w")as f:
            texts[Name] = {"Total_Count": "0", "Accuracy": "0%"}
            json.dump(texts,f)
        coincounting(Name)

def usercreated():
        Name = input("Name: ")
        if Name in texts:
            Total_Count = (texts[Name]["Total_Count"])
            Accuracy = (texts[Name]["Accuracy"])
            Correct = (texts[Name]["Correct"])
            DATA["Name1"] = Name
            DATA["Total_count"] = Total_Count
            DATA["Accuracy"] = Accuracy
            DATA["Correct"] = Correct
            coincounting(Name)
        else:
            print("Name not found")
            sleep(1) 
            menu() 
    
def update_file(count, accuracy_percentage,correct,Name):
    texts[Name] = {"Total_Count": count, "Accuracy": accuracy_percentage, "Correct": correct}
    with open("Coin_count.json", "w") as f:
        json.dump(texts,f)
    print("Data Saved")
    sleep(1)
    menu()

def allvolunteers(): #Prints all volunteers saves in the file
    print(texts)
    sleep(5)
    menu()

def accuracy(count,correct): #Calculates the accuracy in percentage
    accuracy = correct / count 
    accuracy2 = accuracy *100
    accuracy_percentage = round(accuracy2)
    return accuracy_percentage 

def coincounting(Name): #Main part of the code that counts the coins and asks
    i = input("How many bags do you want to count? ")
    while not i.isdigit():
        print("Invalid input")
        i = input("How many bags do you want to count? ")
    i = int(i)
    correct = 0
    count = 0
    while count != i:
        try:
            Coin = float(input("What is the value of the coin in the bag? (Please use 0.00 to indicate) "))
        except:
            print("Invalid data entered please retry") 
            continue
        else:
            if Coin not in COINTYPE:
                Coin = print("Invalid coin type please re-enter")
                sleep(1)
                continue
        Weight = float(input("What is the weight of the bag? "))
        Real_Coin = COIN_DICTIONARY["Coin Weight"][Coin]
        Bag_weight = COIN_DICTIONARY["Bag weight"][Coin]
        count += 1
        result = Calculator(Weight,Real_Coin,Bag_weight,correct)
        if result is True:
            correct += 1 
    count += int(DATA["Total_count"])
    correct += int(DATA["Correct"])
    accuracy_percentage = accuracy(count,correct)
    sleep(1)
    update_file(count, accuracy_percentage,correct,Name)

def menu():  #Main menu 
    print("""  _____     _        _____               __  _          
 / ___/__  (_)__    / ___/__  __ _____  / /_(_)__  ___ _
/ /__/ _ \/ / _ \  / /__/ _ \/ // / _ \/ __/ / _ \/ _ `/
\___/\___/_/_//_/  \___/\___/\_,_/_//_/\__/_/_//_/\_, / 
                                                 /___/""")
    print()
    
    Choice = input("""
        A: Show all volunteers statistics
        B: Use already excising volunteers
        C: Add new volunteer
        D: End program
                   
    Please enter your choice: """)
    
    if Choice.lower() == "a": 
        allvolunteers()
    elif Choice.lower() == "b" :
        usercreated()
    elif Choice.lower() == "c" :
        adduser()
    elif Choice.lower() == "d" :
        print("Thanks for counting coins")
        sys.exit()
    else:
        print("Invalid option shutting down") 
        sys.exit()

texts = dict()
with open("Coin_count.json", "r") as file:
    texts = json.load(file)
menu()
